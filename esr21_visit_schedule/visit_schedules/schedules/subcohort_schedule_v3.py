from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit as BaseVisit

from ..crfs_requisitions import crf, sub_28_98_requisitions
from ..crfs_requisitions import sub_70_requisitions, requisitions_prns
from ..crfs_requisitions import sub_enrol_requisitions


class Visit(BaseVisit):

    def __init__(self, crfs_unscheduled=None, requisitions_unscheduled=None,
                 crfs_prn=None, requisitions_prn=None,
                 allow_unscheduled=None, **kwargs):
        super().__init__(
            allow_unscheduled=True if allow_unscheduled is None else allow_unscheduled,
            crfs_unscheduled=crfs_unscheduled,
            requisitions_unscheduled=requisitions_unscheduled,
            crfs_prn=crfs_prn or crf.get('crf_prn'),
            requisitions_prn=requisitions_prn or requisitions_prns,
            **kwargs)


# schedule for new participants
esr21_sub_enrol_schedule3 = Schedule(
    name='esr21_sub_enrol_schedule3',
    verbose_name='ESR21 Sub Cohort Enrollment Schedule V3',
    sequence='1',
    onschedule_model='esr21_subject.onschedule',
    offschedule_model='esr21_subject.offschedule',
    consent_model='esr21_subject.informedconsent',
    appointment_model='edc_appointment.appointment')

visit0 = Visit(
    code='1000',
    title='Day 0 Month 1 Visit',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=sub_enrol_requisitions,
    crfs=crf.get('enrollment'),
    facility_name='5-day clinic')

visit1 = Visit(
    code='1028',
    title='Day 28(' + u'\u00B1' + '3) Month 1 Visit',
    timepoint=1,
    rbase=relativedelta(days=28),
    rlower=relativedelta(days=3),
    rupper=relativedelta(days=3),
    requisitions=sub_28_98_requisitions,
    crfs=crf.get('followup'),
    facility_name='5-day clinic')

visit2 = Visit(
    code='1035',
    title='Day 35(' + u'\u00B1' + '3) Month 2 Visit',
    timepoint=2,
    rbase=relativedelta(days=35),
    rlower=relativedelta(days=3),
    rupper=relativedelta(days=3),
    requisitions=None,
    crfs=crf.get('followup'),
    facility_name='5-day clinic')

visit3 = Visit(
    code='1042',
    title='Day 42(' + u'\u00B1' + '3) Month 2 Visit',
    timepoint=3,
    rbase=relativedelta(days=42),
    rlower=relativedelta(days=3),
    rupper=relativedelta(days=3),
    requisitions=None,
    crfs=crf.get('followup'),
    facility_name='5-day clinic')

visit4 = Visit(
    code='1049',
    title='Day 49(' + u'\u00B1' + '3) Month 2 Visit',
    timepoint=4,
    rbase=relativedelta(days=49),
    rlower=relativedelta(days=3),
    rupper=relativedelta(days=3),
    requisitions=None,
    crfs=crf.get('followup'),
    facility_name='5-day clinic')

visit5 = Visit(
    code='1056',
    title='Day 56(' + u'\u00B1' + '3) Month 2 Visit',
    timepoint=5,
    rbase=relativedelta(days=56),
    rlower=relativedelta(days=3),
    rupper=relativedelta(days=3),
    requisitions=None,
    crfs=crf.get('followup'),
    facility_name='5-day clinic')

esr21_sub_enrol_schedule3.add_visit(visit=visit0)
esr21_sub_enrol_schedule3.add_visit(visit=visit1)
esr21_sub_enrol_schedule3.add_visit(visit=visit2)
esr21_sub_enrol_schedule3.add_visit(visit=visit4)
esr21_sub_enrol_schedule3.add_visit(visit=visit5)


esr21_sub_fu_schedule3 = Schedule(
    name='esr21_sub_fu_schedule3',
    verbose_name='ESR21 Sub Cohort Follow Up Schedule V3',
    sequence='2',
    onschedule_model='esr21_subject.onschedule',
    offschedule_model='esr21_subject.offschedule',
    consent_model='esr21_subject.informedconsent',
    appointment_model='edc_appointment.appointment')

visit7 = Visit(
    code='1070',
    title='Day 70(' + u'\u00B1' + '14) Month 3 Visit',
    timepoint=7,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=14),
    rupper=relativedelta(days=14),
    requisitions=sub_70_requisitions,
    crfs=crf.get('day_70_170'),
    facility_name='5-day clinic')

visit8 = Visit(
    code='1098',
    title='Day 98(' + u'\u00B1' + '3) Month 3 Visit',
    timepoint=8,
    rbase=relativedelta(days=28),
    rlower=relativedelta(days=3),
    rupper=relativedelta(days=3),
    requisitions=sub_28_98_requisitions,
    crfs=crf.get('followup'),
    facility_name='5-day clinic')

esr21_sub_fu_schedule3.add_visit(visit=visit7)
esr21_sub_fu_schedule3.add_visit(visit=visit8)

esr21_sub_boost_schedule = Schedule(
    name='esr21_sub_boost_schedule',
    verbose_name='ESR21 Sub Cohort Booster Schedule V3',
    sequence='3',
    onschedule_model='esr21_subject.onschedule',
    offschedule_model='esr21_subject.offschedule',
    consent_model='esr21_subject.informedconsent',
    appointment_model='edc_appointment.appointment')

visit9 = Visit(
    code='1170',
    title='Day 170(' + u'\u00B1' + '14) Month 6 Visit',
    timepoint=9,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=14),
    rupper=relativedelta(days=14),
    requisitions=sub_70_requisitions,
    crfs=crf.get('day_70_170'),
    facility_name='5-day clinic')

visit10 = Visit(
    code='1198',
    title='Day 198(' + u'\u00B1' + '3) Month 6 Visit',
    timepoint=10,
    rbase=relativedelta(days=28),
    rlower=relativedelta(days=3),
    rupper=relativedelta(days=3),
    requisitions=None,
    crfs=crf.get('followup'),
    facility_name='5-day clinic')

visit11 = Visit(
    code='1273',
    title='Day 273(' + u'\u00B1' + '3) Month 9 Visit',
    timepoint=11,
    rbase=relativedelta(days=103),
    rlower=relativedelta(days=3),
    rupper=relativedelta(days=3),
    requisitions=None,
    crfs=crf.get('followup'),
    facility_name='5-day clinic')

visit12 = Visit(
    code='1364',
    title='Day 364(' + u'\u00B1' + '3) Month 12 Visit',
    timepoint=12,
    rbase=relativedelta(days=194),
    rlower=relativedelta(days=3),
    rupper=relativedelta(days=3),
    requisitions=None,
    crfs=crf.get('followup'),
    facility_name='5-day clinic')


esr21_sub_boost_schedule.add_visit(visit=visit9)
esr21_sub_boost_schedule.add_visit(visit=visit10)
esr21_sub_boost_schedule.add_visit(visit=visit11)
esr21_sub_boost_schedule.add_visit(visit=visit12)
