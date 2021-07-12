from edc_visit_schedule import VisitSchedule, site_visit_schedules

from .schedules import esr21_enrollment_schedule, esr21_fu_schedule
from .schedules import esr21_sub_enrollment_schedule
from .schedules import esr21_illness_schedule, esr21_sub_fu_schedule

esr21_visit_schedule = VisitSchedule(
    name='esr21_visit_schedule',
    verbose_name='ESR21',
    offstudy_model='esr21_prn.subjectoffstudy',
    locator_model='esr21_subject.personalcontactinfo',
    death_report_model='esr21_prn.deathreport',
    previous_visit_schedule=None)

esr21_visit_schedule.add_schedule(esr21_enrollment_schedule)
esr21_visit_schedule.add_schedule(esr21_fu_schedule)
esr21_visit_schedule.add_schedule(esr21_sub_enrollment_schedule)
esr21_visit_schedule.add_schedule(esr21_sub_fu_schedule)
esr21_visit_schedule.add_schedule(esr21_illness_schedule)

site_visit_schedules.register(esr21_visit_schedule)
