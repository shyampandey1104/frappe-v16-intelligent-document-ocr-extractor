# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "intelligent_doc_ocr"
app_title = "Frappe v16 Intelligent Document Processing & OCR Extractor"
app_publisher = "Shyamkumar Pandey"
app_description = "Frappe v16 AI-powered Intelligent Document Processing (IDP) engine for automated PDF invoice, purchase order, and bill of lading text parsing, tabular line extraction, and automated Frappe DocType ingestion."
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"
required_frappe_version = ">=16.0.0"

# Includes in <head>
app_include_css = "/assets/intelligent_doc_ocr/css/intelligent_doc_ocr.bundle.css"
app_include_js = "/assets/intelligent_doc_ocr/js/intelligent_doc_ocr.bundle.js"

# Document Events
doc_events = {
    "Frappe v16 Intelligent Document Processing & OCR Extractor Entry": {
        "validate": "intelligent_doc_ocr.services.validator.EnterpriseValidationEngine.validate_compliance_rules",
        "on_submit": "intelligent_doc_ocr.services.integration_service.EnterpriseIntegrationService.verify_remote_status"
    }
}

# Scheduled Background Tasks
scheduler_events = {
    "hourly": [
        "intelligent_doc_ocr.tasks.hourly_sync"
    ],
    "daily": [
        "intelligent_doc_ocr.tasks.daily_reconciliation"
    ],
    "weekly": [
        "intelligent_doc_ocr.tasks.weekly_digest"
    ]
}
