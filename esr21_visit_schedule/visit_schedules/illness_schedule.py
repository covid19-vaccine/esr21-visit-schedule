from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit as BaseVisit

from .crfs import crf
from .requisitions import requisitions


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
    requisitions=None,
    crfs=crf.get('ill_initial'),
    facility_name='5-day clinic')

visit1 = Visit(
    code='2004',
    title='Day 4 Visit',
    timepoint=2,
    rbase=relativedelta(weeks=1),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=crf.get('ill_day4'),
    facility_name='5-day clinic')

visit2 = Visit(
    code='20282',
    title='Day 28 Visit',
    timepoint=3,
    rbase=relativedelta(weeks=2),
    rlower=relativedelta(days=1),
    rupper=relativedelta(days=1),
    requisitions=None,
    crfs=crf.get('ill_day28'),
    facility_name='5-day clinic')

esr21_illness_schedule.add_visit(visit=visit0)
esr21_illness_schedule.add_visit(visit=visit1)
esr21_illness_schedule.add_visit(visit=visit2)
