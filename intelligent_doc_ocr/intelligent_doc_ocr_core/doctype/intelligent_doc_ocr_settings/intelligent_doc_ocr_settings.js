frappe.ui.form.on("Frappe v16 Intelligent Document Processing & OCR Extractor Settings", {
    refresh: function(frm) {
        frm.add_custom_button(__("Test v16 Connection"), function() {
            frm.call({ doc: frm.doc, method: "test_connection" });
        });
    }
});
