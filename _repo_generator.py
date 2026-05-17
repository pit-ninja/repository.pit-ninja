import os
import hashlib
import xml.etree.ElementTree as ET

class Generator:
    def __init__(self):
        self.generate_addons_file()
        self.generate_md5_file()
        print("Repository generated successfully.")

    def generate_addons_file(self):
        addons_root = ET.Element("addons")
        
        # Walk through all directories in the repo
        for d in os.listdir("."):
            if os.path.isdir(d) and not d.startswith("."):
                addon_xml_path = os.path.join(d, "addon.xml")
                if os.path.exists(addon_xml_path):
                    try:
                        tree = ET.parse(addon_xml_path)
                        root = tree.getroot()
                        addons_root.append(root)
                    except Exception as e:
                        print(f"Error parsing {addon_xml_path}: {e}")

        # Write the combined addons.xml
        tree = ET.ElementTree(addons_root)
        ET.indent(tree, space="  ", level=0)
        tree.write("addons.xml", encoding="utf-8", xml_declaration=True)

    def generate_md5_file(self):
        try:
            m = hashlib.md5()
            with open("addons.xml", "rb") as f:
                m.update(f.read())
            with open("addons.xml.md5", "w") as f:
                f.write(m.hexdigest())
        except Exception as e:
            print(f"An error occurred creating the MD5 file: {e}")

if __name__ == "__main__":
    Generator()
