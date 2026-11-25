// Frappe v16 Client Script for Frappe v16 Intelligent Document Processing & OCR Extractor Entry
frappe.ui.form.on("Frappe v16 Intelligent Document Processing & OCR Extractor Entry", {
    refresh: function(frm) {
        if (frm.doc.status === "Submitted") {
            frm.page.set_indicator(__("v16 Verified"), "green");
        }
        if (frm.doc.docstatus === 1) {
            frm.add_custom_button(__("View v16 Audit Trail"), function() {
                frappe.set_route("List", "Frappe v16 Intelligent Document Processing & OCR Extractor Audit Log");
            }, __("v16 Actions"));
        }
    }
});
