import unittest
from intelligent_doc_ocr.engine import DocumentOCRExtractor

class TestDocumentOCRExtractor(unittest.TestCase):
    def setUp(self):
        self.extractor = DocumentOCRExtractor()

    def test_invoice_parsing_and_doc_conversion(self):
        sample_text = """
        TAX INVOICE
        Vendor: Global Logistics Ltd
        Invoice No: INV-2026-8812
        Date: 2026-05-14
        Grand Total: $2,000.00
        """
        data = self.extractor.extract_invoice_fields(sample_text)
        self.assertEqual(data["invoice_number"], "INV-2026-8812")
        self.assertEqual(data["invoice_date"], "2026-05-14")
        self.assertEqual(data["total_amount"], 2000.0)

        doc = self.extractor.convert_to_frappe_purchase_invoice(data)
        self.assertEqual(doc["doctype"], "Purchase Invoice")
        self.assertEqual(doc["bill_no"], "INV-2026-8812")
        self.assertEqual(len(doc["items"]), 2)

if __name__ == "__main__":
    unittest.main()
