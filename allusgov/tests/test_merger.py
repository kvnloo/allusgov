"""Tests for provenance tracking across sequential tree merges."""

import logging
from io import StringIO

from bigtree import Node

from allusgov.exporter.exporter import TextExporter
from allusgov.merger.merger import Merger


def source_tree(source_name: str, include_lab: bool = False) -> Node:
    """Build a small source tree with stable source-specific attributes."""
    root = Node(
        "US FEDERAL GOVERNMENT",
        **{source_name: {"name": "US FEDERAL GOVERNMENT"}},
    )
    agency = Node(
        f"[{source_name}] Environmental Protection Agency",
        parent=root,
        **{source_name: {"name": "Environmental Protection Agency"}},
    )
    if include_lab:
        Node(
            f"[{source_name}] Research Lab",
            parent=agency,
            **{source_name: {"name": "Research Lab"}},
        )
    return root


def test_provenance_survives_sequential_merges_and_text_export(tmp_path):
    """Matched and transferred nodes retain every contributing source."""
    logger = logging.getLogger(__name__)
    base = source_tree("samgov")
    opm = source_tree("opmgov", include_lab=True)

    merged = Merger(
        logger=logger,
        base_tree=base,
        base_name="samgov",
        source_tree=opm,
        source_name="opmgov",
        threshold=90,
    ).merge()

    usa = source_tree("usagov", include_lab=True)
    merged = Merger(
        logger=logger,
        base_tree=merged,
        base_name="samgov",
        source_tree=usa,
        source_name="usagov",
        threshold=90,
    ).merge()

    agency = merged.children[0]
    lab = agency.children[0]

    assert merged.get_attr("sources") == ["samgov", "opmgov", "usagov"]
    assert agency.get_attr("sources") == ["samgov", "opmgov", "usagov"]
    assert lab.get_attr("sources") == ["opmgov", "usagov"]

    output = StringIO()
    exporter = TextExporter(
        logger=logger,
        source="merged",
        tree=merged,
        data_dir=str(tmp_path),
    )
    exporter.print_tree(merged, "merged", output)
    rendered = output.getvalue()

    assert " - samgov, opmgov, usagov" in rendered
    assert " - opmgov, usagov" in rendered
    assert ", sources" not in rendered
