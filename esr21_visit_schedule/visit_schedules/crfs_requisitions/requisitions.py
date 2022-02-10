from edc_visit_schedule import FormsCollection, Requisition
from esr21_labs import humoral_immunogenicity_panel, sars_pcr_panel, urine_hcg_panel
from esr21_labs import wb_cmi_panel, hematology_panel, sars_serum_panel

# Main Study Requisitions
main_vax1_requisitions = FormsCollection(
    Requisition(
        show_order=10,
        panel=sars_pcr_panel, required=False, additional=False),
    Requisition(
        show_order=20,
        panel=urine_hcg_panel, required=False, additional=False),
    )
main_vax2_requisitions = FormsCollection(
    Requisition(
        show_order=10,
        panel=sars_pcr_panel, required=True, additional=False),
    Requisition(
        show_order=20,
        panel=urine_hcg_panel, required=True, additional=False),
    Requisition(
        show_order=30,
        panel=wb_cmi_panel, required=True, additional=False),
    )

main_fu_requisitions = FormsCollection(
    Requisition(
        show_order=10,
        panel=wb_cmi_panel, required=True, additional=False),)

# Subcohort Requisitions
sub_post_vax_requisitions = FormsCollection(
    Requisition(
        show_order=10,
        panel=sars_pcr_panel, required=True, additional=False),
    Requisition(
       show_order=20,
       panel=urine_hcg_panel, required=True, additional=False),
    Requisition(
        show_order=30,
        panel=wb_cmi_panel, required=True, additional=False),
    Requisition(
        show_order=40,
        panel=humoral_immunogenicity_panel, required=True, additional=False),)

sub_enrol_requisitions = FormsCollection(
    Requisition(
        show_order=10,
        panel=humoral_immunogenicity_panel, required=True, additional=False),
    Requisition(
        show_order=20,
        panel=wb_cmi_panel, required=True, additional=False),
    Requisition(
       show_order=30,
       panel=urine_hcg_panel, required=False, additional=False),)

sub_fu_requisitions = FormsCollection(
    Requisition(
        show_order=10,
        panel=sars_serum_panel, required=True, additional=False),)

sub_28_98_requisitions = FormsCollection(
    Requisition(
        show_order=10,
        panel=wb_cmi_panel, required=True, additional=False),
    Requisition(
        show_order=20,
        panel=humoral_immunogenicity_panel, required=True, additional=False),)

sub_70_requisitions = FormsCollection(
    Requisition(
        show_order=10,
        panel=sars_pcr_panel, required=True, additional=False),
    Requisition(
        show_order=20,
        panel=sars_serum_panel, required=True, additional=False),
    Requisition(
       show_order=30,
       panel=urine_hcg_panel, required=True, additional=False),
    Requisition(
        show_order=40,
        panel=wb_cmi_panel, required=True, additional=False),
    Requisition(
        show_order=50,
        panel=humoral_immunogenicity_panel, required=True, additional=False),
    )

sub_182_requisitions = FormsCollection(
    Requisition(
        show_order=10,
        panel=sars_serum_panel, required=True, additional=False),
    Requisition(
        show_order=20,
        panel=wb_cmi_panel, required=True, additional=False),
    Requisition(
        show_order=30,
        panel=humoral_immunogenicity_panel, required=True, additional=False),)

sub_fu2_requisitions = FormsCollection(
    Requisition(
        show_order=10,
        panel=sars_serum_panel, required=True, additional=False),
    Requisition(
        show_order=20,
        panel=humoral_immunogenicity_panel, required=True, additional=False))

# Illness Requisitions
ill_0_requisitions = FormsCollection(
    Requisition(
        show_order=10,
        panel=sars_pcr_panel, required=True, additional=False),
    Requisition(
        show_order=20,
        panel=sars_serum_panel, required=True, additional=False),
    Requisition(
        show_order=30,
        panel=wb_cmi_panel, required=True, additional=False),
    Requisition(
        show_order=40,
        panel=humoral_immunogenicity_panel, required=True, additional=False),
    )

ill_28_requisitions = FormsCollection(
    Requisition(
        show_order=10,
        panel=wb_cmi_panel, required=True, additional=False),
    Requisition(
        show_order=20,
        panel=humoral_immunogenicity_panel, required=True, additional=False),
    )
