from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit as BaseVisit

from ..crfs_requisitions import crf, sub_post_vax3_requisitions, post_vax_requisitions
from ..crfs_requisitions import sub_post_vax_requisitions, sub_fu_requisitions, illness_requisitions
from ..crfs_requisitions import sub_fu2_requisitions, post_vax2_requisitions


class Visit(BaseVisit):

    def __init__(self, crfs_unscheduled=None, requisitions_unscheduled=None,
                 crfs_prn=None, requisitions_prn=None,
                 allow_unscheduled=None, **kwargs):
        super().__init__(
            allow_unscheduled=True if allow_unscheduled is None else allow_unscheduled,
            crfs_unscheduled=crfs_unscheduled,
            requisitions_unscheduled=requisitions_unscheduled,
            crfs_prn=crfs_prn,
            requisitions_prn=requisitions_prn,
            **kwargs)


# schedule for new participants
esr21_sub_enrollment_schedule = Schedule(
    name='esr21_sub_enrol_schedule',
    verbose_name='ESR21 Sub Cohort Enrollment Schedule',
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
    requisitions=sub_post_vax_requisitions,
    crfs=crf.get('enrollment'),
    facility_name='5-day clinic')

esr21_sub_enrollment_schedule.add_visit(visit=visit0)

esr21_sub_fu_schedule = Schedule(
    name='esr21_sub_fu_schedule',
    verbose_name='ESR21 Sub Cohort Follow Up Schedule',
    onschedule_model='esr21_subject.onschedule',
    offschedule_model='esr21_subject.offschedule',
    consent_model='esr21_subject.informedconsent',
    appointment_model='edc_appointment.appointment')

visit1 = Visit(
    code='1007',
    title='Day 7(' + u'\u00B1' + '3) Month 1 Visit',
    timepoint=1,
    rbase=relativedelta(weeks=1),
    rlower=relativedelta(days=3),
    rupper=relativedelta(days=3),
    requisitions=sub_fu_requisitions,
    crfs=crf.get('followup'),
    facility_name='5-day clinic')

visit2 = Visit(
    code='1014',
    title='Day 14(' + u'\u00B1' + '3) Month 1 Visit',
    timepoint=2,
    rbase=relativedelta(weeks=2),
    rlower=relativedelta(days=3),
    rupper=relativedelta(days=3),
    requisitions=sub_fu_requisitions,
    crfs=crf.get('followup'),
    facility_name='5-day clinic')

visit3 = Visit(
    code='1021',
    title='Day 21(' + u'\u00B1' + '3) Month 1 Visit',
    timepoint=3,
    rbase=relativedelta(weeks=3),
    rlower=relativedelta(days=3),
    rupper=relativedelta(days=3),
    requisitions=None,
    crfs=crf.get('followup'),
    facility_name='5-day clinic')

visit4 = Visit(
    code='1028',
    title='Day 28(' + u'\u00B1' + '3) Month 1 Visit',
    timepoint=4,
    rbase=relativedelta(weeks=4),
    rlower=relativedelta(days=3),
    rupper=relativedelta(days=3),
    requisitions=illness_requisitions,
    crfs=crf.get('followup'),
    facility_name='5-day clinic')

visit5 = Visit(
    code='1035',
    title='Day 35(' + u'\u00B1' + '3) Month 2 Visit',
    timepoint=5,
    rbase=relativedelta(days=35),
    rlower=relativedelta(days=3),
    rupper=relativedelta(days=3),
    requisitions=None,
    crfs=crf.get('followup'),
    facility_name='5-day clinic')

visit6 = Visit(
    code='1042',
    title='Day 42(' + u'\u00B1' + '3) Month 2 Visit',
    timepoint=6,
    rbase=relativedelta(days=42),
    rlower=relativedelta(days=3),
    rupper=relativedelta(days=3),
    requisitions=None,
    crfs=crf.get('followup'),
    facility_name='5-day clinic')

visit7 = Visit(
    code='1049',
    title='Day 49(' + u'\u00B1' + '3) Month 2 Visit',
    timepoint=7,
    rbase=relativedelta(days=49),
    rlower=relativedelta(days=3),
    rupper=relativedelta(days=3),
    requisitions=None,
    crfs=crf.get('followup'),
    facility_name='5-day clinic')

visit8 = Visit(
    code='1056',
    title='Day 56(' + u'\u00B1' + '3) Month 2 Visit',
    timepoint=8,
    rbase=relativedelta(days=56),
    rlower=relativedelta(days=3),
    rupper=relativedelta(days=3),
    requisitions=None,
    crfs=crf.get('followup'),
    facility_name='5-day clinic')

visit9 = Visit(
    code='163',
    title='Day 63(' + u'\u00B1' + '3) Month 3 Visit',
    timepoint=9,
    rbase=relativedelta(days=63),
    rlower=relativedelta(days=3),
    rupper=relativedelta(days=3),
    requisitions=None,
    crfs=crf.get('followup'),
    facility_name='5-day clinic')

visit10 = Visit(
    code='1070',
    title='Day 70(' + u'\u00B1' + '3) Month 3 Visit',
    timepoint=10,
    rbase=relativedelta(days=70),
    rlower=relativedelta(days=3),
    rupper=relativedelta(days=3),
    requisitions=post_vax2_requisitions,
    crfs=crf.get('day_70'),
    facility_name='5-day clinic')

visit11 = Visit(
    code='1077',
    title='Day 77(' + u'\u00B1' + '3) Month 3 Visit',
    timepoint=11,
    rbase=relativedelta(days=77),
    rlower=relativedelta(days=3),
    rupper=relativedelta(days=3),
    requisitions=None,
    crfs=crf.get('followup'),
    facility_name='5-day clinic')

visit12 = Visit(
    code='1084',
    title='Day 84(' + u'\u00B1' + '3) Month 3 Visit',
    timepoint=12,
    rbase=relativedelta(days=84),
    rlower=relativedelta(days=3),
    rupper=relativedelta(days=3),
    requisitions=None,
    crfs=crf.get('followup'),
    facility_name='5-day clinic')

visit13 = Visit(
    code='1091',
    title='Day 91(' + u'\u00B1' + '3) Month 3 Visit',
    timepoint=13,
    rbase=relativedelta(days=91),
    rlower=relativedelta(days=3),
    rupper=relativedelta(days=3),
    requisitions=None,
    crfs=crf.get('followup'),
    facility_name='5-day clinic')

visit14 = Visit(
    code='1098',
    title='Day 98(' + u'\u00B1' + '3) Month 3 Visit',
    timepoint=14,
    rbase=relativedelta(days=98),
    rlower=relativedelta(days=3),
    rupper=relativedelta(days=3),
    requisitions=illness_requisitions,
    crfs=crf.get('followup'),
    facility_name='5-day clinic')

visit15 = Visit(
    code='1182',
    title='Day 182(' + u'\u00B1' + '3) Month 6 Visit',
    timepoint=15,
    rbase=relativedelta(days=182),
    rlower=relativedelta(days=3),
    rupper=relativedelta(days=3),
    requisitions=sub_post_vax3_requisitions,
    crfs=crf.get('followup'),
    facility_name='5-day clinic')

visit16 = Visit(
    code='1273',
    title='Day 273(' + u'\u00B1' + '3) Month 9 Visit',
    timepoint=16,
    rbase=relativedelta(days=273),
    rlower=relativedelta(days=3),
    rupper=relativedelta(days=3),
    requisitions=sub_fu2_requisitions,
    crfs=None,
    facility_name='5-day clinic')

visit17 = Visit(
    code='1364',
    title='Day 364(' + u'\u00B1' + '3) Month 12 Visit',
    timepoint=17,
    rbase=relativedelta(days=364),
    rlower=relativedelta(days=3),
    rupper=relativedelta(days=3),
    requisitions=sub_fu2_requisitions,
    crfs=crf.get('followup'),
    facility_name='5-day clinic')

esr21_sub_fu_schedule.add_visit(visit=visit1)
esr21_sub_fu_schedule.add_visit(visit=visit2)
esr21_sub_fu_schedule.add_visit(visit=visit3)
esr21_sub_fu_schedule.add_visit(visit=visit4)
esr21_sub_fu_schedule.add_visit(visit=visit5)
esr21_sub_fu_schedule.add_visit(visit=visit6)
esr21_sub_fu_schedule.add_visit(visit=visit7)
esr21_sub_fu_schedule.add_visit(visit=visit8)
esr21_sub_fu_schedule.add_visit(visit=visit9)
esr21_sub_fu_schedule.add_visit(visit=visit10)
esr21_sub_fu_schedule.add_visit(visit=visit11)
esr21_sub_fu_schedule.add_visit(visit=visit12)
esr21_sub_fu_schedule.add_visit(visit=visit13)
esr21_sub_fu_schedule.add_visit(visit=visit14)
esr21_sub_fu_schedule.add_visit(visit=visit15)
esr21_sub_fu_schedule.add_visit(visit=visit16)
esr21_sub_fu_schedule.add_visit(visit=visit17)
