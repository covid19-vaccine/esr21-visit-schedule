from edc_visit_schedule import FormsCollection, Requisition
from esr21_labs import wb_cmi_panel, hematology_panel, sars_serum_panel
from esr21_labs import humoral_immunogenicity_panel, sars_pcr_panel

illness_requisitions = FormsCollection(
    Requisition(
        show_order=10,
        panel=wb_cmi_panel, required=True, additional=False),
    Requisition(
        show_order=20,
        panel=humoral_immunogenicity_panel, required=True, additional=False),)

sample_collection_requisitions = FormsCollection(
    Requisition(
        show_order=10,
        panel=sars_pcr_panel, required=True, additional=False),)

post_vax2_requisitions = FormsCollection(
    Requisition(
        show_order=10,
        panel=sars_pcr_panel, required=True, additional=False),
    Requisition(
        show_order=20,
        panel=sars_serum_panel, required=True, additional=False),
    Requisition(
        show_order=30,
        panel=wb_cmi_panel, required=True, additional=False),)

post_vax_requisitions = FormsCollection(
    Requisition(
        show_order=10,
        panel=sars_pcr_panel, required=True, additional=False),
    Requisition(
        show_order=20,
        panel=wb_cmi_panel, required=True, additional=False),)

whole_blood_requisitions = FormsCollection(
    Requisition(
        show_order=10,
        panel=wb_cmi_panel, required=True, additional=False),)

sub_fu_requisitions = FormsCollection(
    Requisition(
        show_order=10,
        panel=sars_serum_panel, required=True, additional=False),)

sub_fu2_requisitions = FormsCollection(
    Requisition(
        show_order=10,
        panel=sars_serum_panel, required=True, additional=False),
    Requisition(
        show_order=20,
        panel=sars_pcr_panel, required=True, additional=False))
