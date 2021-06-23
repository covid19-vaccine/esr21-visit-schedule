from edc_visit_schedule import FormsCollection, Crf

crf = {}

crfs_initial = FormsCollection(
    Crf(show_order=1, model='esr21_subject.azd1222vaccination'),
    Crf(show_order=2, model='esr21_subject.vaccinationdetails'),
    Crf(show_order=3, model='esr21_subject.demographicsdata'),
    Crf(show_order=4, model='esr21_subject.medicalhistory'),
    Crf(show_order=5, model='esr21_subject.rapidhivtesting'),
    Crf(show_order=6, model='esr21_subject.pregnancytest',
        required=False),
    Crf(show_order=7, model='esr21_subject.pregnancystatus',
        required=False),
    Crf(show_order=8, model='esr21_subject.physicalexam'),
    Crf(show_order=9, model='esr21_subject.covid19preventivebehaviors'),
    name='enrollment',
)

crfs_followup = FormsCollection(
    Crf(show_order=1, model='esr21_subject.adverseevent'),
    Crf(show_order=2, model='esr21_subject.pregnancy'),
    Crf(show_order=3, model='esr21_subject.pregnancystatus'),
    name='followup',
)

crfs_day_70 = FormsCollection(
    Crf(show_order=1, model='esr21_subject.azd1222vaccination'),
    Crf(show_order=2, model='esr21_subject.vaccinationdetails'),
    Crf(show_order=3, model='esr21_subject.pregnancy'),
    Crf(show_order=4, model='esr21_subject.pregnancystatus'),
    Crf(show_order=5, model='esr21_subject.physicalexam'),
    name='day_70',
)

crf.update({'enrollment': crfs_initial,
            'day_70': crfs_day_70,
            'followup': crfs_followup, })
