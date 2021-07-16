from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit as BaseVisit

from ..crfs_requisitions import crf, illness_requisitions


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


# first schedule for ill participants
esr21_illness_schedule = Schedule(
    name='esr21_illness_schedule',
    verbose_name='ESR21 Illness Visits Schedule',
    onschedule_model='esr21_subject.onscheduleill',
    offschedule_model='esr21_subject.offschedule',
    consent_model='esr21_subject.informedconsent',
    appointment_model='edc_appointment.appointment')

visit0 = Visit(
    code='2000',
    title='Day 0 Visit',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=illness_requisitions,
    crfs=crf.get('ill_initial'),
    facility_name='5-day clinic')

visit1 = Visit(
    code='2004',
    title='Day 4 Visit',
    timepoint=1,
    rbase=relativedelta(days=4),
    rlower=relativedelta(days=2),
    rupper=relativedelta(days=2),
    requisitions=None,
    crfs=crf.get('ill_day4'),
    facility_name='5-day clinic')

visit2 = Visit(
    code='2028',
    title='Day 28 Visit',
    timepoint=2,
    rbase=relativedelta(days=28),
    rlower=relativedelta(days=1),
    rupper=relativedelta(days=1),
    requisitions=illness_requisitions,
    crfs=crf.get('ill_day28'),
    facility_name='5-day clinic')

esr21_illness_schedule.add_visit(visit=visit0)
esr21_illness_schedule.add_visit(visit=visit1)
esr21_illness_schedule.add_visit(visit=visit2)

# Second schedule for ill participants
esr21_illness2_schedule = Schedule(
    name='esr21_illness2_schedule',
    verbose_name='ESR21 Illness Visits 2 Schedule',
    onschedule_model='esr21_subject.onscheduleill',
    offschedule_model='esr21_subject.offschedule',
    consent_model='esr21_subject.informedconsent',
    appointment_model='edc_appointment.appointment')

esr21_illness2_schedule.add_visit(visit=visit0)
esr21_illness2_schedule.add_visit(visit=visit1)
esr21_illness2_schedule.add_visit(visit=visit2)

# Third schedule for ill participants
esr21_illness3_schedule = Schedule(
    name='esr21_illness3_schedule',
    verbose_name='ESR21 Illness Visits 3 Schedule',
    onschedule_model='esr21_subject.onscheduleill',
    offschedule_model='esr21_subject.offschedule',
    consent_model='esr21_subject.informedconsent',
    appointment_model='edc_appointment.appointment')

esr21_illness3_schedule.add_visit(visit=visit0)
esr21_illness3_schedule.add_visit(visit=visit1)
esr21_illness3_schedule.add_visit(visit=visit2)

# Fourth schedule for ill participants
esr21_illness4_schedule = Schedule(
    name='esr21_illness4_schedule',
    verbose_name='ESR21 Illness Visits 4 Schedule',
    onschedule_model='esr21_subject.onscheduleill',
    offschedule_model='esr21_subject.offschedule',
    consent_model='esr21_subject.informedconsent',
    appointment_model='edc_appointment.appointment')

esr21_illness4_schedule.add_visit(visit=visit0)
esr21_illness4_schedule.add_visit(visit=visit1)
esr21_illness4_schedule.add_visit(visit=visit2)

# Fifth schedule for ill participants
esr21_illness5_schedule = Schedule(
    name='esr21_illness5_schedule',
    verbose_name='ESR21 Illness Visits 5 Schedule',
    onschedule_model='esr21_subject.onscheduleill',
    offschedule_model='esr21_subject.offschedule',
    consent_model='esr21_subject.informedconsent',
    appointment_model='edc_appointment.appointment')

esr21_illness5_schedule.add_visit(visit=visit0)
esr21_illness5_schedule.add_visit(visit=visit1)
esr21_illness5_schedule.add_visit(visit=visit2)

# Sixth schedule for ill participants
esr21_illness6_schedule = Schedule(
    name='esr21_illness6_schedule',
    verbose_name='ESR21 Illness Visits 6 Schedule',
    onschedule_model='esr21_subject.onscheduleill',
    offschedule_model='esr21_subject.offschedule',
    consent_model='esr21_subject.informedconsent',
    appointment_model='edc_appointment.appointment')

esr21_illness6_schedule.add_visit(visit=visit0)
esr21_illness6_schedule.add_visit(visit=visit1)
esr21_illness6_schedule.add_visit(visit=visit2)

# Seventh schedule for ill participants
esr21_illness7_schedule = Schedule(
    name='esr21_illness7_schedule',
    verbose_name='ESR21 Illness Visits 7 Schedule',
    onschedule_model='esr21_subject.onscheduleill',
    offschedule_model='esr21_subject.offschedule',
    consent_model='esr21_subject.informedconsent',
    appointment_model='edc_appointment.appointment')

esr21_illness7_schedule.add_visit(visit=visit0)
esr21_illness7_schedule.add_visit(visit=visit1)
esr21_illness7_schedule.add_visit(visit=visit2)

# Eighth schedule for ill participants
esr21_illness8_schedule = Schedule(
    name='esr21_illness8_schedule',
    verbose_name='ESR21 Illness Visits 8 Schedule',
    onschedule_model='esr21_subject.onscheduleill',
    offschedule_model='esr21_subject.offschedule',
    consent_model='esr21_subject.informedconsent',
    appointment_model='edc_appointment.appointment')

esr21_illness8_schedule.add_visit(visit=visit0)
esr21_illness8_schedule.add_visit(visit=visit1)
esr21_illness8_schedule.add_visit(visit=visit2)

# Ninth schedule for ill participants
esr21_illness9_schedule = Schedule(
    name='esr21_illness9_schedule',
    verbose_name='ESR21 Illness Visits 9 Schedule',
    onschedule_model='esr21_subject.onscheduleill',
    offschedule_model='esr21_subject.offschedule',
    consent_model='esr21_subject.informedconsent',
    appointment_model='edc_appointment.appointment')

esr21_illness9_schedule.add_visit(visit=visit0)
esr21_illness9_schedule.add_visit(visit=visit1)
esr21_illness9_schedule.add_visit(visit=visit2)

# Tenth schedule for ill participants
esr21_illness10_schedule = Schedule(
    name='esr21_illness10_schedule',
    verbose_name='ESR21 Illness Visits 10 Schedule',
    onschedule_model='esr21_subject.onscheduleill',
    offschedule_model='esr21_subject.offschedule',
    consent_model='esr21_subject.informedconsent',
    appointment_model='edc_appointment.appointment')

esr21_illness10_schedule.add_visit(visit=visit0)
esr21_illness10_schedule.add_visit(visit=visit1)
esr21_illness10_schedule.add_visit(visit=visit2)

# Eleventh schedule for ill participants
esr21_illness11_schedule = Schedule(
    name='esr21_illness11_schedule',
    verbose_name='ESR21 Illness Visits 11 Schedule',
    onschedule_model='esr21_subject.onscheduleill',
    offschedule_model='esr21_subject.offschedule',
    consent_model='esr21_subject.informedconsent',
    appointment_model='edc_appointment.appointment')

esr21_illness11_schedule.add_visit(visit=visit0)
esr21_illness11_schedule.add_visit(visit=visit1)
esr21_illness11_schedule.add_visit(visit=visit2)

# Twelfth schedule for ill participants
esr21_illness12_schedule = Schedule(
    name='esr21_illness12_schedule',
    verbose_name='ESR21 Illness Visits 12 Schedule',
    onschedule_model='esr21_subject.onscheduleill',
    offschedule_model='esr21_subject.offschedule',
    consent_model='esr21_subject.informedconsent',
    appointment_model='edc_appointment.appointment')

esr21_illness12_schedule.add_visit(visit=visit0)
esr21_illness12_schedule.add_visit(visit=visit1)
esr21_illness12_schedule.add_visit(visit=visit2)
