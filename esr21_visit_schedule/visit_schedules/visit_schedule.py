from edc_visit_schedule import VisitSchedule, site_visit_schedules

from .schedule import esr21_enrollment_schedule, esr21_fu_schedule
from .illness_schedule import esr21_illness_schedule

esr21_visit_schedule = VisitSchedule(
    name='esr21_visit_schedule',
    verbose_name='ESR21',
    offstudy_model='esr21_prn.subjectoffstudy',
    locator_model='esr21_subject.personalcontactinfo',
    death_report_model='esr21_prn.deathreport',
    previous_visit_schedule=None)

esr21_visit_schedule.add_schedule(esr21_enrollment_schedule)
esr21_visit_schedule.add_schedule(esr21_fu_schedule)
# esr21_visit_schedule.add_schedule(esr21_illness_schedule)

site_visit_schedules.register(esr21_visit_schedule)
