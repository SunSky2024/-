#!/usr/bin/env python3
"""Extract selected causal inference slide pages as PNG figures.

The script is intentionally configured to export only key review pages, not
whole decks. Page numbers in LECTURE_PAGES are 1-based PDF page numbers.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import fitz  # PyMuPDF
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit(
        "PyMuPDF is required. Install it with: python -m pip install pymupdf"
    ) from exc


LECTURE_PAGES = {
    "10": [
        {"page": 14, "name": "g_formula"},
        {"page": 20, "name": "iptw_intro"},
        {"page": 26, "name": "iptw_pseudo_population"},
        {"page": 40, "name": "doubly_robust_estimator"},
        {"page": 55, "name": "causal_dag"},
        {"page": 58, "name": "backdoor_collider_path"},
        {"page": 71, "name": "conditioning_on_collider"},
        {"page": 73, "name": "d_separation"},
        {"page": 77, "name": "backdoor_criterion"},
        {"page": 78, "name": "dag_adjustment_examples"},
    ],
    "11": [
        {"page": 5, "name": "longitudinal_dag"},
        {"page": 8, "name": "null_paradox_dag"},
        {"page": 15, "name": "mean_msm_weights"},
        {"page": 16, "name": "iptw_weights"},
        {"page": 18, "name": "iptw_procedure"},
        {"page": 21, "name": "cox_msm_estimating_equation"},
        {"page": 30, "name": "time_varying_setup"},
        {"page": 34, "name": "two_stage_snm"},
        {"page": 40, "name": "msm_snm_dag"},
        {"page": 42, "name": "msm_snm_comparison"},
    ],
    "12": [
        {"page": 12, "name": "iv_dag"},
        {"page": 21, "name": "wald_estimand"},
        {"page": 25, "name": "compliance_types"},
        {"page": 29, "name": "complier_causal_effect"},
        {"page": 32, "name": "new_drug_trial"},
        {"page": 39, "name": "ace_estimand"},
        {"page": 45, "name": "two_stage_least_squares"},
        {"page": 49, "name": "two_sls_estimated_exposure"},
        {"page": 54, "name": "iv_inequality_test"},
        {"page": 56, "name": "overidentification_tests"},
    ],
}

PDF_FILES = {
    "10": "10.causal_intro_slides.pdf",
    "11": "11.causal_longitudinal_slides.pdf",
    "12": "12.iv_slides.pdf",
}


def slugify(value: str) -> str:
    """Return a readable ASCII filename stem."""
    value = value.strip().lower().replace("-", "_")
    value = re.sub(r"[^a-z0-9_]+", "_", value)
    value = re.sub(r"_+", "_", value).strip("_")
    return value or "slide"


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def default_pdf_root(root: Path) -> Path:
    candidates = [
        root / "ppt",
        root.parent.parent / "ppt",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return candidates[0]


def render_page(pdf_path: Path, page_number: int, output_path: Path, width: int) -> None:
    with fitz.open(pdf_path) as doc:
        if page_number < 1 or page_number > len(doc):
            raise ValueError(
                f"{pdf_path.name} has {len(doc)} pages; requested page {page_number}"
            )
        page = doc[page_number - 1]
        zoom = width / page.rect.width
        matrix = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=matrix, alpha=False)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        pix.save(output_path)


def extract_all(pdf_root: Path, output_root: Path, width: int) -> list[Path]:
    outputs: list[Path] = []
    for lecture, pages in LECTURE_PAGES.items():
        pdf_path = pdf_root / PDF_FILES[lecture]
        if not pdf_path.exists():
            raise FileNotFoundError(f"Missing source PDF: {pdf_path}")

        lecture_dir = output_root / f"lecture_{lecture}"
        lecture_dir.mkdir(parents=True, exist_ok=True)

        for item in pages:
            page_number = int(item["page"])
            stem = f"p{page_number:02d}_{slugify(item['name'])}.png"
            output_path = lecture_dir / stem
            render_page(pdf_path, page_number, output_path, width)
            outputs.append(output_path)
    return outputs


def parse_args() -> argparse.Namespace:
    root = repo_root()
    parser = argparse.ArgumentParser(
        description="Render selected causal inference slide pages as PNG figures."
    )
    parser.add_argument(
        "--pdf-root",
        type=Path,
        default=default_pdf_root(root),
        help="Directory containing the source PDF decks.",
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=root / "notes" / "statistical-learning" / "assets" / "slides",
        help="Directory where lecture_10/11/12 image folders are written.",
    )
    parser.add_argument(
        "--width",
        type=int,
        default=1400,
        help="Target PNG width in pixels.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    pdf_root = args.pdf_root.resolve()
    output_root = args.output_root.resolve()
    outputs = extract_all(pdf_root, output_root, args.width)
    for path in outputs:
        print(path)
    print(f"Extracted {len(outputs)} slide images to {output_root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
