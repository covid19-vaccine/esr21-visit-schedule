from edc_visit_schedule import FormsCollection, Crf

crf = {}

crfs_initial = FormsCollection(
    Crf(show_order=1, model='esr21_subject.demographicsdata'),
    Crf(show_order=2, model='esr21_subject.medicalhistory'),
    Crf(show_order=3, model='esr21_subject.physicalexam'),
    Crf(show_order=4, model='esr21_subject.rapidhivtesting'),
    Crf(show_order=5, model='esr21_subject.pregnancystatus',
        required=False),
    Crf(show_order=6, model='esr21_subject.pregnancytest',
        required=False),
    Crf(show_order=7, model='esr21_subject.vaccinationdetails'),
    Crf(show_order=8, model='esr21_subject.vitalsigns'),
    Crf(show_order=9, model='esr21_subject.covid19preventativebehaviours'),
    name='enrollment',
)

crfs_followup = FormsCollection(
    Crf(show_order=1, model='esr21_subject.adverseevent'),
    Crf(show_order=2, model='esr21_subject.hospitalisation',
        required=False),
    Crf(show_order=3, model='esr21_subject.covid19symptomaticinfections'),
    Crf(show_order=4, model='esr21_subject.pregnancystatus',
        required=False),
    name='followup',
)

crfs_day_70 = FormsCollection(
    Crf(show_order=1, model='esr21_subject.physicalexam'),
    Crf(show_order=2, model='esr21_subject.pregnancytest',
        required=False),
    Crf(show_order=3, model='esr21_subject.pregnancystatus',
        required=False),
    Crf(show_order=4, model='esr21_subject.vaccinationdetails'),
    name='day_70',
)

crfs_ill_initial = FormsCollection(
    Crf(show_order=1, model='esr21_subject.medicalhistory'),
    Crf(show_order=2, model='esr21_subject.physicalexam'),
    Crf(show_order=3, model='esr21_subject.concomitantmedication'),
    Crf(show_order=4, model='esr21_subject.vitalsigns'),
    Crf(show_order=5, model='esr21_subject.covid19symptomaticinfections'),
    Crf(show_order=6, model='esr21_subject.seriousadverseevent',
        required=False),
    name='ill_initial',
)

crfs_ill_4 = FormsCollection(
    Crf(show_order=1, model='esr21_subject.concomitantmedication'),
    Crf(show_order=2, model='esr21_subject.covid19symptomaticinfections'),
    Crf(show_order=3, model='esr21_subject.seriousadverseevent',
        required=False),
    name='ill_day4',
)

crfs_ill_28 = FormsCollection(
    Crf(show_order=1, model='esr21_subject.physicalexam'),
    Crf(show_order=2, model='esr21_subject.concomitantmedication'),
    Crf(show_order=3, model='esr21_subject.vitalsigns'),
    Crf(show_order=4, model='esr21_subject.covid19symptomaticinfections'),
    Crf(show_order=5, model='esr21_subject.seriousadverseevent',
        required=False),
    name='ill_day28',
)

crf.update({'enrollment': crfs_initial,
            'day_70': crfs_day_70,
            'followup': crfs_followup,
            'ill_initial': crfs_ill_initial,
            'ill_day4': crfs_ill_4,
            'ill_day28': crfs_ill_28})
