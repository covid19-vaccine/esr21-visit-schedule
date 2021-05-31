from edc_visit_schedule import FormsCollection, Crf

crf = {}

crfs_initial = FormsCollection(
    Crf(show_order=1, model='esr21_subject.demographicsdata'),
    Crf(show_order=2, model='esr21_subject.medicalhistory'),
    Crf(show_order=3, model='esr21_subject.rapidhivtesting'),
    Crf(show_order=4, model='esr21_subject.pregnancystatus'),
    Crf(show_order=5, model='esr21_subject.covid19preventivebehaviors'),
    name='enrollment',
)

crfs_unscheduled = FormsCollection(
    Crf(show_order=1, model='esr21_subject.vaccinationdetails'),
    Crf(show_order=2, model='esr21_subject.adverseevent'),
    Crf(show_order=3, model='esr21_subject.pregnancystatus'),
    name='week1_10',
)

crfs_followup = FormsCollection(
    Crf(show_order=2, model='esr21_subject.adverseevent'),
    Crf(show_order=3, model='esr21_subject.pregnancystatus'),
    name='followup',
)

crf.update({'enrollment': crfs_initial,
            'week1_10': crfs_unscheduled,
            'followup': crfs_followup, })
