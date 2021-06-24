from edc_visit_schedule import FormsCollection, Requisition
from esr21_labs import wb_cmi_panel, hematology_panel, sars_serum_panel
from esr21_labs import humoral_immunogenicity_panel, sars_pcr_panel

infant_requisitions_prn = FormsCollection(
    name='infant_requisitions_prn')

subject_enrollment_requisitions = FormsCollection(
    Requisition(
        show_order=10, panel=hematology_panel, required=True, additional=True),
    Requisition(
        show_order=20, panel=sars_pcr_panel, required=True, additional=True),
    name='requisitions_1000'
)

infant_1month_requisitions = FormsCollection(
    Requisition(
        show_order=10, panel=infant_insulin, required=True, additional=True),
    Requisition(
        show_order=20, panel=infant_glucose_panel, required=True, additional=True),
    Requisition(
        show_order=30, panel=dna_pcr, required=True, additional=True),
    Requisition(
        show_order=40, panel=serum_panel, required=True, additional=True),
    Requisition(
        show_order=50, panel=infant_pbmc_pl_store_panel, required=True, additional=True),
    Requisition(
        show_order=60, panel=infant_paxgene_panel, required=False, additional=True),
    name='requisitions_2010'
)

infant_followup_requisitions = FormsCollection(
    Requisition(
        show_order=10, panel=dna_pcr, required=False, additional=True),
    name='requisitions_2020'
)
