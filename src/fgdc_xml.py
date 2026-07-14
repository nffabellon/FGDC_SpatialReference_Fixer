"""
FGDC Spatial Reference Fixer

Module:
    fgdc_xml.py

Purpose:
    Read, inspect, update, and save FGDC XML metadata files.
"""

from pathlib import Path
import xml.etree.ElementTree as ET


class FGDCMetadata:

    def __init__(self, xml_file):

        self.xml_file = Path(xml_file)

        if not self.xml_file.exists():
            raise FileNotFoundError(self.xml_file)

        self.tree = ET.parse(self.xml_file)
        self.root = self.tree.getroot()

    # ---------------------------------------------------------
    # Save XML
    # ---------------------------------------------------------

    def save(self, output_file=None):

        if output_file is None:
            output_file = self.xml_file

        self.tree.write(
            output_file,
            encoding="utf-8",
            xml_declaration=True
        )

    # ---------------------------------------------------------
    # Find IDINFO
    # ---------------------------------------------------------

    def get_idinfo(self):

        return self.root.find("idinfo")

    # ---------------------------------------------------------
    # Find SPREF
    # ---------------------------------------------------------

    def get_spref(self):

        return self.root.find("spref")

    # ---------------------------------------------------------
    # Remove existing SPREF
    # ---------------------------------------------------------

    def remove_spref(self):

        node = self.get_spref()

        if node is not None:
            self.root.remove(node)

    # ---------------------------------------------------------
    # Insert SPREF
    # ---------------------------------------------------------

    def insert_spref(self, spref_node):

        self.remove_spref()

        self.root.append(spref_node)

    # ---------------------------------------------------------
    # Return XML Root
    # ---------------------------------------------------------

    def get_root(self):

        return self.root
