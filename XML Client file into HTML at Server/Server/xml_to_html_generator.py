import os.path
import sys
import lxml.etree
import pdfkit
import time

def xml_to_html_transform(input_xml_filename,process_xsl_filename,output_filename):
    """Script for running an XSL transform against an XML file.
    The script accepts three positional arguments:
    (1) The input XML file to process
    (2) The XSL transform to process the XML file with
    (3) The Output file.
    """
    if not os.path.isfile(input_xml_filename):
        print("ERROR: Unable to access input XML file: {0}".format(input_xml_filename))
        sys.exit(1)
    if not os.path.isfile(process_xsl_filename):
        print("ERROR: Unable to access XSL file: {0}".format(process_xsl_filename))
        sys.exit(1)
    if os.path.isfile(output_filename):
        print("WARNING: Output file {0} exists and will be overwritten.".format(output_filename))
    
    input_xml = lxml.etree.parse(input_xml_filename)
    process_xsl = lxml.etree.parse(process_xsl_filename)
    xsl_transform = lxml.etree.XSLT(process_xsl)
    
    output_xml = xsl_transform(input_xml)
    with open(output_filename, 'w') as output_xml_file:
        output_xml_file.write(
            lxml.etree.tostring(
                output_xml,
                pretty_print=True).decode())
