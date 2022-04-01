from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit as BaseVisit

from ..crfs_requisitions import crf, main_vax1_requisitions, main_fu_requisitions
from ..crfs_requisitions import day_70_170_requisitions, requisitions_prns


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
esr21_enrollment_schedule = Schedule(
    name='esr21_enrol_schedule',
    verbose_name='ESR21 Enrollment Schedule',
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
    requisitions=main_vax1_requisitions,
    crfs=crf.get('enrollment'),
    facility_name='5-day clinic')

esr21_enrollment_schedule.add_visit(visit=visit0)

esr21_fu_schedule = Schedule(
    name='esr21_fu_schedule',
    verbose_name='ESR21 Follow Up Schedule',
    onschedule_model='esr21_subject.onschedule',
    offschedule_model='esr21_subject.offschedule',
    consent_model='esr21_subject.informedconsent',
    appointment_model='edc_appointment.appointment')

visit1 = Visit(
    code='1028',
    title='Day 28(' + u'\u00B1' + '3) Month 1 Visit',
    timepoint=1,
    rbase=relativedelta(days=28),
    rlower=relativedelta(days=3),
    rupper=relativedelta(days=3),
    requisitions=main_fu_requisitions,
    crfs=crf.get('followup'),
    facility_name='5-day clinic')

visit2 = Visit(
    code='1070',
    title='Day 70(' + u'\u00B1' + '14) Month 3 Visit',
    timepoint=2,
    rbase=relativedelta(days=70),
    rlower=relativedelta(days=14),
    rupper=relativedelta(days=14),
    requisitions=None,
    crfs=crf.get('day_70_170'),
    facility_name='5-day clinic')

visit3 = Visit(
    code='1098',
    title='Day 98(' + u'\u00B1' + '3) Month 3 Visit',
    timepoint=3,
    rbase=relativedelta(days=98),
    rlower=relativedelta(days=3),
    rupper=relativedelta(days=3),
    requisitions=main_fu_requisitions,
    crfs=crf.get('followup'),
    facility_name='5-day clinic')

esr21_fu_schedule.add_visit(visit=visit1)
esr21_fu_schedule.add_visit(visit=visit2)
esr21_fu_schedule.add_visit(visit=visit3)

esr21_dose2_schedule = Schedule(
    name='esr21_dose2_schedule',
    verbose_name='ESR21 Second Dose Schedule',
    onschedule_model='esr21_subject.onschedule',
    offschedule_model='esr21_subject.offschedule',
    consent_model='esr21_subject.informedconsent',
    appointment_model='edc_appointment.appointment')

visit1070 = Visit(
    code='1070',
    title='Day 70(' + u'\u00B1' + '14) Month 3 Visit',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=day_70_170_requisitions,
    crfs=crf.get('day_70_170'),
    facility_name='5-day clinic')

visit1098 = Visit(
    code='1098',
    title='Day 98(' + u'\u00B1' + '3) Month 3 Visit',
    timepoint=1,
    rbase=relativedelta(days=28),
    rlower=relativedelta(days=3),
    rupper=relativedelta(days=3),
    requisitions=main_fu_requisitions,
    crfs=crf.get('followup'),
    facility_name='5-day clinic')

esr21_dose2_schedule.add_visit(visit=visit1070)
esr21_dose2_schedule.add_visit(visit=visit1098)

esr21_booster_schedule = Schedule(
    name='esr21_booster_schedule',
    verbose_name='ESR21 Booster Schedule',
    onschedule_model='esr21_subject.onschedule',
    offschedule_model='esr21_subject.offschedule',
    consent_model='esr21_subject.informedconsent',
    appointment_model='edc_appointment.appointment')

visit1170 = Visit(
    code='1170',
    title='Day 170(' + u'\u00B1' + '14) Month 6 Visit',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=14),
    rupper=relativedelta(days=14),
    requisitions=day_70_170_requisitions,
    crfs=crf.get('day_70_170'),
    facility_name='5-day clinic')

visit1198 = Visit(
    code='1198',
    title='Day 198(' + u'\u00B1' + '3) Month 6 Visit',
    timepoint=1,
    rbase=relativedelta(days=28),
    rlower=relativedelta(days=3),
    rupper=relativedelta(days=3),
    requisitions=None,
    crfs=crf.get('followup'),
    facility_name='5-day clinic')

visit1273 = Visit(
    code='1273',
    title='Day 273(' + u'\u00B1' + '14) Month 9 Visit',
    timepoint=2,
    rbase=relativedelta(days=103),
    rlower=relativedelta(days=14),
    rupper=relativedelta(days=14),
    requisitions=None,
    crfs=crf.get('followup'),
    facility_name='5-day clinic')

visit1364 = Visit(
    code='1364',
    title='Day 364(' + u'\u00B1' + '14) Month 12 Visit',
    timepoint=3,
    rbase=relativedelta(days=194),
    rlower=relativedelta(days=14),
    rupper=relativedelta(days=14),
    requisitions=None,
    crfs=crf.get('followup'),
    facility_name='5-day clinic')

esr21_booster_schedule.add_visit(visit=visit1170)
esr21_booster_schedule.add_visit(visit=visit1198)
esr21_booster_schedule.add_visit(visit=visit1273)
esr21_booster_schedule.add_visit(visit=visit1364)
