from pipelines import pipeline
import json
intentsfile = json.loads(open('../intents.json').read())


def updatejson(intent):
    a_file = open("../intents.json", "a")
    json.dump(intent ,a_file)
    a_file.write(',')
    a_file.close()


def lastupdateTag():
    a_file = open("../intents.json", "a")
    a_file.write(']}')
    a_file.close()


# nlp = pipeline("multitask-qa-qg")
nlp = pipeline("question-generation", model="valhalla/t5-small-qg-prepend", qg_format="prepend")

# to generate questions simply pass the text
ans = nlp('''Approval Process 2021-22
Frequently Asked Questions
Page | 1
Q : Where to send the queries related to portal and approval related issues for the approval
process 2021-22?
A :
Institute are requested to raises queries only through online Grievance Redressal mechanism
available on AICTE website under Approval Process 2021-22 quick links. No queries through
email will be entertained.
Q : Does AICTE allow Arts and Science Courses in an Institution offering Engineering Courses?
A: Conduct of any other Academic Courses (Technical/Non-Technical):
The Institutions may conduct Academic Courses (Technical/ Non-Technical of any other
Regulatory Body) using the existing facilities in excess or by creating additional facilities as
per the provisions laid down in the norms and standards of the respective Regulatory Body
without affecting the quality of education prescribed by all the Regulatory Bodies after taking
NOC from the Council following the procedure specified in the Approval Process Handbook.
However, the Applicant has to make Material/ Non-Material amendment of the Building Plan,
Site Plan, etc. approved by the concerned Competent Authority (if applicable) to suit the
requirements of the new Programme/ Level.
The total land required shall be the highest amongst the programs/ levels being offered by the
Institute. However, institute shall have sufficient built up area to cover all the requirements
of ALL the programs/ levels conducted as per the provisions of Approval Process Handbook.
The institute shall extends to provide ample space for play-ground (owned or hired) facilities
for indoor and outdoor sports for the students either in the Campus or through arrangements
with other adjacent Institutions, Corporation grounds, private facilities, etc.
Q :
Is it mandatory for an Institution offering Courses in Architecture and Pharmacy to obtain
Approval from AICTE?
A : In compliance of the order dated 08.11.2019 passed by the Hon’ble Supreme Court of Indian
CA No.364/ 2005, for the existing Institutions offering Courses in Architecture Programme,
approval by the Council of Architecture (CoA) is mandatory and AICTE approval is NOT
required.
Approval Process 2021-22
Frequently Asked Questions
Page | 2
In compliance of the order dated 05.03.2020 passed by the Hon’ble Supreme Court of India
in Transferred Petitions (CIVIL) No 87-101 of 2014, for the existing institutions offering
courses in Pharmacy Programme, approval of Pharmacy Council of India (PCI) is mandatory
and AICTE approval is NOT required.
State Public and Private Universities and Central Universities are also not required to take
AICTE approval as per the AICTE Act. However, some of the Universities are seeking approval
of AICTE for availing the benefits of AICTE schemes/initiatives as per the prevailing
policies/norms. Similarly, INTERESTED Architecture and Pharmacy Institutions may apply to
AICTE as a New Institutions or for Extension of Approval (EoA), provided, they are already
having valid approval of CoA and PCI, respectively on the day of application.
Q : Whether establishment of a new Technical Institution to offer Courses in Engineering and
Technology is permissible in Academic Year 2021-22?
A : The Council shall NOT grant approval to New Technical Institutions at the Diploma/ Under
Graduate/ Post Graduate Level in Engineering and Technology in line with the
recommendations of the Committee set up by AICTE to provide National Perspective Plan for
Technical Programmes. However, establishment of New Technical Institutions in Engineering
and Technology shall be permitted only in conditions as specified in Chapter I of APH 2021-
22.
Q : a. Whether MCA/ MBA Department of Arts and Science College is eligible to apply for AICTE
approval?
b. Whether AICTE approval is needed for running MCA Course in our Arts and Science
College?
A : For a and b:
Yes. Refer Clause 1.3.5 of APH 2021-22. In case of non-Technical Institutions seeking
approval for conducting MCA/ MBA and University Departments/ Constituent Colleges
seeking approval for conducting MCA/ MBA/ M.Tech. Programmes apart from their existing
Courses, separate building and Principal are NOT required. However, in such cases all other
Approval Process 2021-22
Frequently Asked Questions
Page | 3
norms (as per APH 2021-22) such as separate Head of the Department, Faculty,
Infrastructure, Built-Up area, etc. should be fulfilled.
Q :
Can we apply for closure of the existing Institution and open a new Institution at the same
premises?
A : Yes. The existing Institution applied for Closure of the Institution are also eligible to apply for
starting a new Technical Institution in the same premises in the same Academic year.
Technical Institutions applying under this Clause shall have to apply for Progressive/
Complete Closure of the Institution for the existing Programme(s) and shall apply for a
different Programme. However, the Applicant has to make Material/ Non-Material
amendment of the Building Plan, Site Plan, etc. duly approved by the concerned Competent
Authority (if applicable) to suit the requirements of the new Programme. In case of change in
Building Plan, the approval of present Competent Authority is required.
Q : Whether a New Institution is obligated to appoint a Principal and Faculty at the time of
application for approval or subsequent to approval before commencement of the Course?
Whether the Faculty to be appointed are for the First Year of the Course or for the entire
period of the Course?
A:
The New Institution is obligated to appoint a Principal and Faculty before the commencement
of the Course. The Faculty to be appointed are for the First Year of the Course and it will be
progressively done each year so that an Expert Visit Committee (EVC) conducted any time
before the first batch of students has passed out, the availability of the facilities of an
Institution as per the norms in Approval Process Handbook shall be verified.
Q : We have been granted LoI in 2020-21 and LoA was rejected. How can we get LoA this year?
A : Applicants issued Letter of Intent (LoI) but rejected after the Expert Visit Committee shall
inform the Council about their readiness of infrastructure after making the payment of TER
Charges as per Clause 1.4.2 of APH 2021-22 through online mode for conduct of another
Expert Visit Committee (EVC). The validity of LoI is Two Years from the year of issue of LoI.
In this case the validity upto 2022-23.
Approval Process 2021-22
Frequently Asked Questions
Page | 4
Q : We have got the first approval for our Institution in 2020-21. But we have NOT admitted
students due the delay in getting affiliation. Do we need to apply for EoA?
A :
ALL the applicants issued LoA for starting the New Technical Institutions shall apply on
AICTE Web-Portal for Extension of Approval (EOA) as specified in the Approval Process
Handbook from the next Academic Year onwards, irrespective of the admission of the
students. However, such institutes need to answer one Question related to this on portal in
order to avoid deficiency.
Q : a. While applying, I had made a mistake in opting for FN/OCI? How can Irectify the mistake?
b. We had applied for the Closure of the Institution, but now we have decided to apply for
EoA. How can I revert the application?
A : For a and b:
You can inform AICTE as per the procedure mentioned in Clause 2.3.8 of APH 2021-22.
Q : We had 25 years of Live Lease at the time of our approval for establishment of new Technical
Institution, currently our Live Lease is 5 years. What should we do to get the EoA?
A :
In case of Institutions having Lease agreement for Land, the Council shall NOT issue EoA
from the Year in which the Live Lease is equal to the number of years of the Course having
the maximum duration. However, if such Institutions submit the Lease extended for further
30 years with at least 25 years of Live Lease, EoA shall be considered.
Q : Our Institution was given Withdrawal of Approval in 2018-19. We are not able to apply
under 2021-22 application.
A : You have to apply ONLY as a New Institution in 2021-22.
Q : a. The Institution has been placed under 20% reduction for 2020-21. How to get the full
Intake in 2021-22?
b. Our Institution was placed under No admission/ No EoA/ Reduction in Intake category in
the previous year. We are not able to create 2021-22 application.
A : For a and b:
Institutions are required to apply for Restoration on the Web Portal.
Q : a. Our Institution got approval up to the Academic Year 2018-19 and we were unable to
submit application in 2019-20 and 2020-21. We want to apply for 2021-22.
Approval Process 2021-22
Frequently Asked Questions
Page | 5
b. We have taken approval from AICTE for the Engineering Courses in 2011-12. After that
we could not take EoA from AICTE due to some reasons. Now we want to apply for EoA in
2021-22. We have ID and password allotted by AICTE in 2011. Should we continue to fill
our application on Web Portal of AICTE using that ID and Password?
c. We have not applied for EoA in the past 3 years. Can we apply for Break in EoA as well as
for a new Programme?
A : a. You are required to apply for Break in EoA on Web Portal. The same user ID and password
can be used.
b. Institutions that have NOT applied for EoA for last SIX YEARS consecutively shall NOT be
eligible to apply under Break in EoA and such Institutions shall apply ONLY as a new
Technical Institution following appropriate procedure for Closure of the Programmes/
Courses approved.
c. The Institutions applying under Break in EoA/ Restoration shall NOT be permitted to apply
for other categories listed under Chapter II/ III/ V/ VI of the APH 2021-22.
Q : Our Intake was reduced to 50% due to the enrollment less than 30% in the past 5 years
consecutively. The student admission this year is more than 30%. Should we have to apply
for Restoration in 2021-22?
A :
The Institution falling under this category need not apply for restoration and the Intake shall
be automatically reinstated by the Council, if the enrolment becomes more than 30% based
on the student enrolment data provided by the Institution on AICTE Portal.
Q : I would like to convert from Diploma to Degree Level and vice-versa. How to do the same?
A : Refer Clause 2.8 of APH 2021-22.
Q : We have 5 Diploma Courses, Can we apply for conversion of Two Diploma Courses only into
Degree Courses?
A : No. Partial conversion of Courses / Programmes at any Levels is NOT permitted.
Q : We are having UG and PG Courses in Engineering and Technology. We would like to apply
for conversion of our Under Graduate Courses into Diploma Level? Should we have to apply
for closure of PG Courses?
Approval Process 2021-22
Frequently Asked Questions
Page | 6
A :
PG Courses in Engineering and Technology should be applied for closure and simultaneously
apply for conversion of UG into Diploma.
Q : We would like to apply for conversion of our UG Degree Courses into Diploma Courses, but
we don’t find the nomenclature of certain Courses in Annexure 3. How can we apply?
A : You have to continue at the same Level or may opt for the closure of Course(s).
Q : We are an Engineering Institution started in 2014-15 with an Intake of 300 seats. We want
to start MBA and MCA Courses in the same Institution with same ID. What is the procedure?
A : You are permitted to apply for ONLY One new Programme/level in an existing Institution.
Q : a. When an existing Institution applies for a new Programme, whether it have to comply
with the built up area and Infrastructural requirements of the new Programme only for First
year and/ or for the entire duration of the new Programme? Whether the existing Institution
and the new Programme can share the administrative and amenities areas by creating
exclusive Instructional area for the new Programme?
b. Whether the existing Institution is entitled for starting only one new Programme and/ or
more than one new Programme in diploma, degree and PG? For example the existing
engineering Institutions wish to start a new Programme of Diploma in Engineering and UG
Design, whether it is possible?
A: a. When an existing Institution applies for a new Programme, it has to comply with the built
up area and Infrastructural requirements of the new Programme only for First year and the
sharing of the administrative and amenities areas are permissible as far as it caters the need
of all the students for all the Programmes, with creation of exclusive instructional area for
the new Programme and progressively done each year to cater the requirement as per AICTE
norms.
b. The Institutions shall be permitted to apply for ANYONE Level (Diploma/ Under Graduate)
in an existing Programme/ a new Programme.
Q : Whether an Institution offering MBA could be merged with an Institution offering
Engineering Courses?
A: Yes, if both the Institutions are run by the same Trust/ Society/ Company.
Q : a. Can we merge two Institutions located within same Campus/City?
b. Can we merge few Courses of a Child Institution with Parent Institution and run the Child
Institution with the remaining Courses?
Approval Process 2021-22
Frequently Asked Questions
Page | 7
c. Can we merge an Institution running Under Graduate Courses and a Polytechnic in
Engineering?
A: For a :
The existing Institutions of the same Trust/ Society/ Company operating in the same location/
city shall be permitted to merge into a single Institution with all the facilities at the proposed
Parent Institution and/ or part/ full facilities of the Child Institution(s), if necessary.
If all the required facilities are available exclusively in the Parent Institution (without
depending on the facilities of the Child Institution(s)), as the Child Institution(s) shall be
considered for Complete Closure. However, the convenience/ approachability of all
stakeholders of the Child Institution(s) to the Site/ Location of the Parent Institution shall also
be taken care of by the Institutions (including commutation). However, the norms of the
concerned Regulatory Bodies shall also be fulfilled (Refer Clause 2.10 of APH 2021-22.)
NOTE: Intra-Day movement of Students and Faculty NOT Allowed under any circumstances
(in case of infrastructure & other facilities required by Parent institution after merger are in
multiple locations). Institutions going for such merger shall duly inform all the stake holders
regarding schedule of conduct of Programs / Courses prior to admission.
b. Not permissible.
c. Yes.
Q : We would like to apply for Conversion of Women’s Institution into Co-ed Institution. But the
enrolment in the last three years is not less than 60%. Are we eligible to apply for the same?
A : You are eligible to apply for Conversion of Women’s Institution into Co-ed Institution, there
is no restriction on the enrolment provided Women Institutions fulfilled the requirement who
Co-ed Institutions as per APH.
Q : How can we apply for Courses in Emerging /Multidisciplinary Areas in Engineering and
Technology?
Approval Process 2021-22
Frequently Asked Questions
Page | 8
A: You can apply for Increase in Intake/ Additional Course(s) in Emerging /Multidisciplinary
Areas, provided the eligibility conditions mentioned in 2.14 and 7.3.2 of APH 2021-22 are
fulfilled.
Q How can we apply for addition seats in Indian / Regional Languages at Diploma/Degree level
Courses in Engineering and Technology?
A: National Education Policy 2020 envisages the availability of Higher Technical Education in
Indian / Regional Languages at Diploma/Degree level. AICTE shall permit an addition of ONE
division with 30/60 seats to the eligible and interested institutes. Institutions seeking approval
shall be permitted for Increase intake ONLY in Accredited courses.
Q : We have One Course with valid NBA accreditation. How many increase/ new Course our
Institution is eligible?
A : Institutions shall be eligible for new Course(s)/ expansion of existing Course(s), equal to the
number of valid NBA accredited Course(s), limited to a maximum of FOUR within the
definition of Division/ Programme/ Level. Refer Clause 2.14.3 of APH 2021-22.
Q : Our Institution has valid NBA accredited Courses. Is it necessary to upload valid NBA letter
on portal and send hard copy to Regional Office?
A : No. However, the information related to validity of NBA accredited Courses need to be
provided on portal. But, your institution need to produce the additional documents including
NBA letter at the time of Scrutiny Committee.
Q : Our Institution has applied for NBA, whether we are eligible for adding a new Course?
A :
Yes, provided accreditation of existing Course is known officially before April 10, 2021 and
subject to the fulfilment of other norms as per APH 2021-22.
Q : Our Institution has obtained Provisional Accreditation for two Courses which are valid till
2019. I have used these Courses for adding two new Courses during 2018-19. If my
Institution secures Provisional accreditation again during 2019 for the same Courses, can I
apply for the introduction of New Course/ increase in Intake using it.
A: No. A Course having valid NBA accreditation can be used for adding New Course/ increase
in Intake only once within a span of 6 years.
Approval Process 2021-22
Frequently Asked Questions
Page | 9
Q : Our Institution has obtained Accreditation for two Courses which are valid till 2018. I have
used these Courses for adding two new Courses during 2017-18. If my Institution got the
renewal of accreditation again afterinspection during 2018 for the same Courses, can I apply
for the introduction of New Course/ increase in Intake using it?
A: Yes. A Course having valid NBA accreditation can be used for adding New Course/ increase
in Intake only once within a span of 6 years. However, if the accreditation of any Course is
renewed after the Inspection by NBA, the Institutions shall utilize the benefit of such
accreditation once again for an increase in the Intake/ Introduction of a new Course.
Q : a. Our Institution is not eligible to apply for NBA accreditation. But we want expansion/ new
Courses how we can apply?
b. Our Engineering Institution started in 2017-18. Could you kindly help with the
information on applying for new Courses?
A : For a and b:
Institutions can apply for new Courses as per Clause 2.14.4 of APH 2021-22.
Q : a. We don’t have accreditation, but we would like to add two Courses one with 30 Intake
and another with 60 Intake by closing a Course with 90 Intake. Is this permissible?
b. Is there any limit on the addition of number of new Courses in lieu of closing existing
Course(s)?
A : For a and b:
ONLY one new course with 30/60 intake in Emerging / Multidisciplinary Areas is possible,
provided the eligibility conditions mentioned in APH 2021-22 Clause 2.14.4 are fulfilled.
Q : We are offering Courses in Design Programme. We are not eligible to apply for NBA. How
can we apply for new PG Course?
Approval Process 2021-22
Frequently Asked Questions
Page | 10
A :
The Institutions offering the Courses in Applied Arts and Crafts and Design shall be eligible
to apply for new Course(s) at the Post Graduate Level only after two batches of students pass
out and the same shall be permitted for a maximum of FIVE Courses/ Divisions, subject to
“Zero Deficiency” based on Self-Disclosure on AICTE Web-Portal. However, for every Post
Graduate Course, there should be at least one Professor with Ph.D. qualification. In case of
non-availability of qualified Professor, an Associate Professor may be considered.
As and when accreditation for the above Courses is started by the NBA, such Institutions who
have been approved by the AICTE to run Course(s) at the Post Graduate Level shall obtain
NBA accreditation within TWO years.
Q : a. Whether a few of the existing Courses shall be continued, while introducing few new
Courses?
b. Whether the maximum permissible Intake after the closure of certain existing Courses
and introduction of certain new Courses shall be the existing Intake of the academic year
2020-21 or the maximum of 300?
c. Whether the Faculty and the Infrastructural facilities for the new Course and / or increase
in Intake in the existing Course are to be for the First Year of the new Course and / or
increase in Intake or for the entire duration of the new Course and / or Intake?
A: For a and b:
Yes. The existing Institution without NBA Accreditation can apply for closure of few existing
Courses in the Programme and introduce new Courses in the same Programme at same Level,
without exceeding the total “Approved Intake”/ “Maximum Intake Allowed”, as applicable,
as well as the number of Courses/ Divisions as specified in Appendix 3 of the Approval
Process Handbook, subject to “Zero Deficiency” based on Self-Disclosure on AICTE Web
Portal. An Expert Visit Committee may be conducted, any time before the first batch of
students has passed out, to verify the fulfilment of the norms as specified in the Approval
Process Handbook.
c. The Faculty, Infrastructural facilities and other requirements have to be fulfilled for the
new Course and / or increase in Intake in the existing Course for the First Year of the new
Course and/ or increase in Intake. An Expert Visit Committee may be conducted, any time
Approval Process 2021-22
Frequently Asked Questions
Page | 11
before the first batch of students has passed out, to verify the fulfilment of the norms as
specified in the Approval Process Handbook.
Q : Our Institution is not eligible to apply for NBA accreditation and we have 5 Courses with total
Intake of 300. Can we start a new Course by closing one existing Course?
A : Yes. Provided the overall enrolment in the A/Y 2019-20 is greater than 50% & NIL
Deficiency on Portal based on Self-Disclosure.
Q : We are a private Polytechnic Institution approved last year, running 5 branches with 300
Intake. Now we want to apply for Increase in Intake and add for new Courses. How many
Courses we can add?
A : You cannot add any new Branch/Course or increase in Intake. Institutions already with
Maximum Intake Allowed, but NOT eligible to apply for NBA for any of their courses, shall
apply for closure of Course(s) and apply for increase in Intake/ new Course within the
maximum permissible Intake as per APH 2021-22. Refer Clause 2.14.4 of APH 2021-22.
Q : Is Integrated M.E./ M.Tech. Programme permitted?
A : Yes. Refer Clause 2.15 of APH 2021-22 for eligible conditions.
Q : We are offering Courses in Engineering and Technology. We would like to offer allied
Vocational Courses. What is the procedure?
A: Institutionsshall be permitted to conduct Vocational Course. Please refer Chapter VI Clause
6.1 of APH 2021-22
Q:
Can we merge Production Engineering Course with Intake 60 and Mechanical Engineering
Course with Intake 60, to offer a single Course in Mechanical Engineering with Intake 120?
A: Merger of Courses as per Broad Classification as per Annexure- 6 / 7 (Diploma or UG Level)
of APH 2021-22 is ONLY Permitted.
Q : We have Three Divisions in Computer Science Engineering and Three Divisions in
Information Technology. Can we get Six Divisions in Computer Science Engineering after
merging?
Approval Process 2021-22
Frequently Asked Questions
Page | 12
A : Merging is permitted as per the nomenclatures given in Annexure 6, so that the Intake after
merging shall be equal to the sum total of the individual Courses and Divisions, subject to
the condition that total number of Divisions after merging per Course shall NOT exceed
THREE Divisions (180), provided the Faculty student ratio be maintained. Refer Clause 2.18
of APH 2021-22.
Q : Can we merge B.E. Electrical Engineering Course with B.E. Computer Science Engineering
Course?
A : Not permissible. Refer Annexure 6 of APH 2021-22 for the Courses permitted for merging.
Q : We want to apply for reduction in Intake within a Division for certain Courses. What is the
maximum number of UG and PG Courses, we can opt for reduction?
A : There is no limit, any number of UG and PG Courses may be selected. However, the reduction
in intake (value) within division is allowed ONLY as per the Provisions of APH 2021-22.
Q : We, Polytechnic Institution, want to reduce the Intake one of Course namely Electronics and
Telecommunication Engineering from 60 to 30. Can we do the same?
A: In any Course, within a Division, (non-Zero) reduction (i.e. 60 to 30) is permissible.
Q: Our Institution wants to change the name of the Course. What is the procedure?
A: Refer Clause 2.18 of APH 2021-22.
Q : Our Institution has become a University. Do we have to apply as a new University under
Chapter I or can we apply for EoA as a University?
A : You can apply for EOA as a University with change of Type of Institution (No need to apply
as a new University under Chapter I). Refer Clause 2.19 of APH 2021-22. However, change
of status will be applicable from next Academic Year
Q : In a State, if one University is merged with another University (by State Government), how
to change the name of the affiliating University under Course Tab.
Approval Process 2021-22
Frequently Asked Questions
Page | 13
A : Select the Question available under Questionnaire “Do you wish to change the Affiliating
University?” Then select the answer as “Yes” and select the name of new affiliating
University from the drop down menu. Contact Approval Bureau along with a request letter
in the Letter head of the Institution enclosing copies of State Government resolution/
Gazette Notification. In such cases, NOC form State Government/ University are not
required.
Q : Name of our affiliating University does not appear in the affiliating University drop down.
A : Contact Approval Bureau for inclusion of the University name in the portal. Send an email
of Institution representation on the Letter head to helpdeskab@aicte-india.org
Q : Our Institution was approved as a Private/ Un-aided Institution. Recently our Institution has
been recognized as minority Institution. How to update this change in AICTE Portal?
A : You can apply on the Portal for Change of Minority Status. Refer Clause 2.20 of APH 2021-
22.
Q : Our Institution has extended EoA upto 2022. When we apply in the Portal for Increase in
Intake, the Portal is calculating the TER Charges. Are we not exempted from payment?
A :
Institutions approved for extended EoA are waived from paying TER Charges for Extension
of Approval (EoA) ONLY for the extended years for the existing Programme(s) and
Course(s) at the time of issue of Extended EoA. However, such Institutions are required to
submit the application for EoA and maintain ALL the norms and standards as specified in
the Approval Process Handbook. In the subsequent years (within the duration of Extended
EOA), if the Institution intends to apply for any other categories, the corresponding TER
Charges as per Approval Process Handbook shall be paid.
Q : What is the last date of submission of hard copy application at Regional Office for the
applications?
A : HARD COPIES OF THE APPLICATION/ ADDITIONAL DOCUMENTS NEED NOT BE
SUBMITTED TO THE REGIONAL OFFICE. As per APH 2021-22, ANY DOCUMENTS NEEDS
TO BE SUBMITTED / REQUIRED then such documents shall be Digitally Signed & uploaded
on AICTE web portal. Applications other than those for Extension of Approval to be
processed by the Scrutiny/ Re-Scrutiny Committee shall present their application and ALL
Approval Process 2021-22
Frequently Asked Questions
Page | 14
original documents along with self-attested copies before the Committee (if offline). Refer
APH for the documents (as applicable) to be uploaded in the Web-Portal.
Q : Whether a State Technical University is required to take approval of AICTE to conduct
Technical Courses.
A :
State Universities do not require prior approval of AICTE to commence a new Department
or Course and Programme(s) in Technical Education, however Universities have obligation
or duty to conform to the standards; and norms laid down by the AICTE from time to time.
Q : a. Ours is a Deemed to be University/ Private University established under UGC Act offering
Technical Programmes but not seeking approval from AICTE. What is the procedure for
getting the Programmes approved by AICTE?
b. Our University is 07 years old Private University approved by UGC. Whether Private
University running technical Programmes/ Courses in Engineering, Management,
Architecture, MCA, etc. are required to obtain AICTE approval?
A: For a:
Institutions Deemed to be Universities seeking approval for the first time from AICTE (in
compliance to the order dated 03.11.2017 passed by the Hon’ble Supreme Court Order CA
No. 17869-17870 / 2017) shall submit an application as a new Technical Institution.
Private Universities interested in seeking approval for the first time from AICTE may submit
an application as a new Technical Institution.
For b: State Private Universities do not require prior approval of AICTE to commence a new
Course and Programme(s) in Technical Education (Engineering, Management, etc.),
however State Private Universities have the obligation or duty to conform to the standards
and norms laid down by the AICTE from time to time.
State Private Universities interested in seeking approval for the first time from AICTE may
submit an application as a new Technical Institution.
Refer Chapter-4 of APH 2021-22 for more DETAILS.
Approval Process 2021-22
Frequently Asked Questions
Page | 15
Q :
We are Standalone Institutions offering PGDM Courses. Can we apply for ODL and/or
Online Courses?
A: Yes. Subject to fulfilling eligibility conditions mentioned in Chapter- 5 of APH 2021-22.
Refer Chapter 5 of APH 2021-22 for more details.
Q : We would like to apply for a new Course, but the nomenclature is not available in the drop
down. How to apply?
A :
If any Institution proposes to start a new Course whose nomenclature is not available in
Appendix 2 of the Approval Process Handbook, prior concurrence, as the case may be, by
the Council for the same shall be necessary. For such concurrence, the Institution with due
endorsement by the Registrar/ Director of affiliating University/ Board/ Technical
Institution shall submit detailed Syllabus and Curriculum and its nomenclature to the Policy
and Academic Planning Bureau, AICTE before 30th September of the Calendar Year, to
process the same in the respective Board. Only Recommended Courses Nomenclatures will
be included in in the ensuing year APH.
Q :
Is Adjunct Faculty being considered for the requisite Faculty Student ratio?
A: In case of Planning - 30% and Design - 20%, Adjunct Faculty/ Resource Persons are
permissible, since the Programme requires exhaustive practical field exposure. In all other
Programmes, ONLY under exigent conditions such as relieving/ retirement of Faculty
members/ delay in Faculty recruitment, Institutions may avail the services of Adjunct
Faculty/ Resource Persons up to a maximum of 10% of the required Faculty members as
per the “Approved Intake”, for a period not exceeding one Academic Session. Refer
Annexure 9 for the Guidelines for the appointment of Adjunct Faculty/ Resource Persons.
Q : Whether Faculty not recruited on Regular basis shall be considered for Faculty Student ratio?
A :
The contractual Faculty who have taught for 2 consecutive semesters in the preceding
Academic Year on Full Time basis ONLY shall be considered for the purpose of calculation
of Faculty.
Q : a. Can we convert our First and Second Shift Diploma Courses into Degree Courses?
Approval Process 2021-22
Frequently Asked Questions
Page | 16
b. We were running First Shift (180) and Second Shift (120), currently the portal shows a
single number with both the Intakes. Because of this, we are getting deficiencies. Please
change the Intake as that of the last year.
A : For a and b :
The Courses offered in the timings of Regular Shift, First Shift, Second Shift and Part Time
shall be considered as Regular Courses. The Institutions shall have to fulfil all facilities such
as Infrastructure, Faculty and other requirements to offer the Regular Courses as per the
norms specified in the Approval Process Handbook for the Total Approved Intake and the
Institutions may conduct the Courses in the timings of Regular Shift, First Shift, Second Shift
and Part Time not exceeding the “Approved Intake” of each Course, as per the convenience
of all stakeholders. All such Institutions shall create the necessary Faculty, Infrastructure
and other facilities WITHIN 2 YEARS to fulfil the norms (before the completion of A/Y 2021-
22). Student enrolment details shall be uploaded in the Web-Portal. Hence the Council will
consider the issue of EoA till such time.
Q : a. Our Institution wants to make admission under Lateral Entry in Engineering and
Technology. Is there any provision in APH 2021-22?
b. Whether Lateral Entry is permitted in Diploma?
c. Whether students from SAARC Countries/ Foreign Nationals are permitted to admit under
Lateral Entry in Engineering Courses?
A : For a, b and c :
Refer Clause 7.14 of APH 2021-22.
Q : We have an Approved Intake of 60 seats in Electronics and Communication Engineering in
UG Course. Now we want to reduce the Intake by 30 in Electronics and Communication
Engineering and in lieu of it can we would like to add the one Division of 30 students in
lateral entry in Engineering UG Course.
A : It is NOT permissible.
Q : Whether our Institution can start ITI with same Infrastructure available in our Polytechnic?
Approval Process 2021-22
Frequently Asked Questions
Page | 17
A: Yes. Refer Chapter VII of APH 2021-22. The Institutions may conduct skill development
Courses of any other Regulatory Body using the existing facilities, or by creating additional
facilities as per the provisions laid down in the norms and standards of the respective
Regulatory Bodies without affecting the quality of education prescribed by both Regulatory
Bodies after taking NOC from the Council.
Q : What is the duration of MCA Course? Lateral Entry Permissible in MCA?
A: Two Years. Hence Lateral Entry is NOT permissible.
Q :
For Under Graduate Degree Programme in Engineering Technology, whether Diploma
qualified students will also be considered on par with students passed 10+2 examination?
A: Yes, in addition to that Students passed Diploma (in Engineering and Technology) will be
considered, subject to vacancies in the First Year, in case the vacancies at lateral entry are
exhausted.
Q : How do we implement the rationalization of nomenclature suggested by the AICTE in
Management Programme?
A:
The nomenclature of the Courses in Management after rationalization will be visible in your
application. The revised nomenclatures are also communicated to all Universities. In case
of difficulty in adopting the nomenclatures, the respective University shall be contacted or
if the issue persists, raise your grievance in the Portal.
Q : Our Institution has six UG Engineering Courses. How many Seminar Halls we need for
running UG Programme?
A : Please Refer Appendix 4 of APH 2021-22.
Q : Do we need Research Laboratory for each PG Course?
A : No. Research Laboratory is to be provided for each Institution offering Post Graduate
Courses.
Q : How the Mega and Metro Cities, Urban Area and Rural Area have been determined?
A : The classification of cities has been made as per Census 2011 data.
Q : We are running Five PG Courses in Civil Engineering. How many Professors with Ph.D.
qualification are required?
Approval Process 2021-22
Frequently Asked Questions
Page | 18
A : For every PG Course, there should be at least one Professor with Ph.D. qualification. Refer
Appendix 7 of APH 2021-22.
Q : What is the Faculty Student ratio to be maintained by the Institutions Deemed to be
Universities/ Institutions having Accreditation/ Autonomous status?
A: Institutions Deemed to be Universities/ Institutions having Accreditation (of one or any
number of Courses)/ Autonomy status shall have Faculty: Student as 1:15 in Under
Graduate Degree Level in Engineering and Technology Courses and maintain a better Cadre
ratio in order to achieve excellence in Technical Education. All such Institutions shall create
the necessary Faculty, Infrastructure and other facilities WITHIN 2 YEARS to fulfil the
norms.
Hence the Council will consider the issue of EoA till such time.
Q :
In Appendix10 subscription of journals, what is N?
A: N is the Total number of Courses. Please read the foot note made available below the table
of Appendix 10.
Q : With reference to APH 2021-22, whether subscription of E-journal is mandatory.
A : Refer Appendix 10 of APH 2021-22. Subscription of the journal will add value to the quality
of Technical education and skill. However, subscription of E-Journals is mandatory for the
Institutions offering PG Courses.
Q :
I want to know whether any applicant of the Organization can be the owner of the land or
else if any member of the organization can give a lease to the applicant society. Moreover,
does the lease agreement needed to be registered or not.
A : Refer Appendix 16.1 of APH 2021-22.
Q :
Is it essential to have representative of AICTE in the Board of Governors?
A :
The suggested composition of Board of Governors for the AICTE approved Institutions has
been given in Appendix 18 of APH 2021-22. Nominee of the All India Council for Technical
Education is mandatory to PGDM Institutions Only.
Approval Process 2021-22
Frequently Asked Questions
Page | 19
Q : Please clarify the qualification and age limit of Adjunct Faculty. Whether a same Adjunct
Faculty can be associated with different Institutions? Is there any restriction for Maximum
no of Institutions that an Adjunct Faculty should be associated?
A : Refer Annexure 9 of APH 2021-22. Adjunct Faculty shall not be engaged in not more than
two Institutions at the same time.
Q :
Can we charge the Fee as per the Recommendation of National Fee Committee given in APH
2021-22?
A :
Institutions have to contact the respective State Fee Regulatory Committee for finalizing the
Fee.
Q : How much is the Development Fee is recommended by the National Fee Committee?
A : No split up for Development Fee is available in the report of the National Fee Committee.
Q : What is the procedure for conversion of Technical Institution into Technical Campus?
A : There is no provision to convert a Technical Institution into Technical Campus. You can
refer Clause 2.9 of APH 2021-22 for starting a new Programme/ Level in the existing
Institutions. The Institutions shall be permitted to apply for ANYONE Level (Diploma/
Under Graduate) in an existing Programme/ a new Programme, not exceeding THREE
Division(s)/ Course(s). However, the norms of the concerned Regulatory Authorities shall
also be fulfilled. Also, refer Merger of Institutions Clause in APH 2021-22.
Q : We want to change the details which are non-editable/ read-only. How this can be done?
A : If the Institution intend to modify the Non-Editable fields such as Land details, etc. shall
contact AICTE HQ (Approval Bureau) with supporting documents.
Q : Whether Affidavit can be submitted in e-Stamp Paper?
A : Yes, as well as physical stamp paper.
Q : Is TER Charges refundable if application is rejected?
A :
TER Charges shall not be refunded in any case, if the application is processed and rejected
as specified in the Approval Process Handbook. However, if application is rejected at the
Approval Process 2021-22
Frequently Asked Questions
Page | 20
Level of Scrutiny/ Re-Scrutiny (as per Clause 1.6 of APH 2021-22) without availing the
appeal provision, TER Charges as applicable shall be refunded to the Applicant/ Institution.
Q : When we have established our Institution in 1980, we have got the Completion Certificate
issued by the then Competent Authority, but we don’t have Occupancy Certificate for 2018.
How can we apply for EoA?
A : Your Completion Certificate is acceptable. Structural Stability Certificate from the
registered Structural Engineer is to be submitted after the expiry of a period of thirty years
from the issue of Completion Certificate.
Q : How to get a copy of Corrigendum EoA / Corrigendum LoA in case of corrections made in
EoA or LoA from AICTE Web Portal?
A : Institution need to check drop down menu and click on ‘Corrigendum EoA’ or ‘Corrigendum
LoA’ as the case may be, instead of clicking on ‘EoA’ or ‘LoA’ menu.
Q : Whether e-Affidavit is mandatory?
A :
E-affidavit is preferable NOT mandatory.
Q : How can an Institution apply for National Digital Library?
A: Ministry of Human Resource Development under its National Mission on Education through
Information and Communication Technology (NMEICT) has initiated the National Digital
Library (NDL) pilot project to develop a framework of virtual repository of learning
resources with a single window search facility. The pilot project is devising a framework
suitable for future scale up with respect to content volume and diversity to become a fullblown National Digital Library of India over time. It is being developed at IIT Kharagpur.
To apply, Institutions has to log on to https:/ / ndl.iitkgp.ac.in/ and go to Institutional
Registration. It is offered at absolute Free of Cost.
Q : What is National Academic Depository? How to apply?
Approval Process 2021-22
Frequently Asked Questions
Page | 21
A: NAD is a Unique, Innovative and Progressive step towards achieving Digital enablement of
the Education Records. NAD aspires to make the vision of Digital Academic Certificates for
every Indian a reality. NAD is not only a database copy of the certificate records for
Academic Institutions but a complete system for Issuing Online Certificates to well identified
and registered students. It will be an active online place for Students, Academic Institutions
and Verification Users. To apply, Institutions shall log on to https:/nad.ndml.in/
aboutnad.html and proceed towards the link “New Registrations”.
Q : What is Food and Safety Act 2006? How to comply with its norms?
A:
It is an act under Ministry of Law and Justice to consolidate the laws relating to food and to
establish the Food Safety and Standards Authority of India for laying down science based
standards for articles of food and to regulate their manufacture, storage, distribution, sale
and import, to ensure availability of safe and wholesome food for human consumption and
for matters connected therewith or incidental thereto. The provision under the act is
available at http:/ / www.fssai.gov.in/ home/ fss-legislation/ food-safety-and-standardsact.html.
The Canteen/ Mess running in all AICTE approved Institutions should obtain a certificate
from the Local Self Government/ any other Competent Authority stating that the same is
complying with the norms and standards mentioned in the Act.
Q : Is it necessary to provide details for Quality Education Mandate?
A: Yes. It is mandate for all the Institutions.
Q: Is it permitted to change Minority status to Non Minority?
A: Yes, it is possible as per Clause 2.20.2 of APH 2021-22
Q:
If a Central University taking approval for engineering programme at PG Level only and
running Management, MCA programme is it mandatory to take approval of AICTE for all
other technical programme?
A: Yes, it is mandatory, no partial approval for the programme/ course issued to Universities
from A.Y. 2021-22 as per Clause 4.3.3 of APH 2021-22
Q: Is DSC mandatory for submission of online application for New and Existing Institutions?
A: Yes, it is mandatory, as per Clause 1.4.3 of APH 2021-22
Approval Process 2021-22
Frequently Asked Questions
Page | 22
Q: Existing institutions can start new programme/ level in engineering?
A:
Existing institutions can start New engineering program only in emerging area courses as
per Clause 1.9.1 (a) of APH 2021-22
Q Whether AICTE will give approval for Technical courses at Diploma /Degree level in
Regional language?
A: Yes, Additional division of 30/60 seats in Regional languages against each valid NBA
accredited courses as per Clause 2.14.2 of APH 2021-22.
Q: Is there any TER charges applicable for starting Vocational courses under NSQF?
A: No TER charges for starting New Vocational courses under NSQF.
Q:
It is possible to have Collaboration and Twinning programme between Two Indian
Institutions/ Indian and Foreign Universities?
A: Yes, As per the Clause 3.2 of APH 2021-22 Institutions fulfilling the conditions are eligible
to start program/ courses under Collaboration and Twinning.
Q: What are the requirements of Infrastructure for Online education compared to ODL
education?
A: Refer Clause 5.2.5 of APH 2021-22 to know about infrastructure requirements.
Q: Whether Govt aided Technical institutions running self-financing courses need to pay TER
Charges ?
A: No, as per Cause 2.3.3 of APH 2021-22. Government Aided Institutions are Exempted from
payment of TER Charges ONLY from this A/Y 2021-22.
Q: Whether TIN/GST number for any Industry is Mandatory in order to have MoU with AICTE
approved Institutions?
A: YES. Refer Clause 7.22 of APH 2021-22.
Q: Whether Lateral entry admission is considered forthe enrolment calculation under reduction
in intake category of punitive action.
A: Yes, Institute having less than 50% admission in last 5 years along with lateral entry
admission is considered as per Clause 7.13 (a) of APH 2021-22.
Approval Process 2021-22
Frequently Asked Questions
Page | 23
Q Whether any institution can conduct a course or program affiliated to two different
Universities?
A: No, As per Clause 2.14.6 of APH 2021-22.
Q
Clarify whether a two years old AICTE approved institution with intake of 120 can apply for
increase in intake up to 180 seats without NBA Accreditation?
A
Yes, up to 180 (three divisions) in different courses. However, total intake more than 300
shall NOT be permitted.
Q
Whether Standalone B.HMCT college can apply for closure and start New program in same
establishment ?
A Yes. Simultaneous Closure of One Program and Opening of New Program Permitted.
Q What is the procedure to start MCA Program in a University?
A
Universities are permitted to Start any Technical Program (including MCA) without prior
approval of AICTE. However, all the University need to maintain Norms & Standards
prescribed by AICTE for running such programs from time to time.
Q
Is it necessary to have two seminar halls and Office with 300 Sq.Mts for running MBA and
MCA Courses.
A Refer Appendix 4 of APH 2021-22
Q
A State Govt University running 3 Programs (MBA, MCA and B. Arch). Is it necessary to
take approval of AICTE for running these Programmes?
A
It is optional for State Govt. University to take Approval of AICTE for running any of the
above mentioned Programs. However, they need to maintain Standards and Norms
prescribed by Concerned Regulatory Authorities.
Q
Provide list of courses / areas that can be offered / started in ODL / OL mode by existing
Standalone Engineering Institutions.
A
Please refer Clause 5.1 of APH 2021-22 (Chapter-5). Affiliated Engineering Institutes are
NOT permitted to Offer ODL / OL Courses.
Q
After the Merger of two courses under the same Major Disciple as per 2.18.1.c, Page No 59,
what will be the allowed maximum intake?
A
Intake after merger shall be equal to the sum total of individual courses, subject to the
condition that total no of divisions after merger should NOT exceed 3 Divisions.
Approval Process 2021-22
Frequently Asked Questions
Page | 24
Q
Courses on Emerging areas like AI & DS, CSE (DS), CSE (AI &ML) etc. are not mentioned in
Annexure 6 of APH under Major Discipline CS & E. Whether All such courses will be
permitted as emerging area courses under the Major Discipline of CS&E in A/Y 2021-22 or
NOT?
A
Only AI and DS can be offered as full-fledged Emerging Area Course. Rest can be offered
ONLY as a Minor / Hons. under CSE.
Q
We would like to apply for two new courses, one in B.E CSE (AI and ML) and the other one
in B.E CSE (Data Science) under CSE department which is already running B.E. CSE for
which SAR submitted to NBA.
A
B.E CSE (AI and ML) and B.E CSE (Data Science) can be offered as a Minor / Hons under
existing CSE Course.
Q
Please enlightened us, regarding how to produce quality students with good technical
knowledge
A
AICTE is already having Margdarshak and Margdarshan Schemes. The institute having
Marg Darshak are taking care of nearby institution for enhancing the quality of technical
education to produce quality students.
Q
As there are no parameters mentioned in hand book for Pharmacy. How can we fill the
extension of approval form for Pharmacy?
A
Provision is made available on portal for the Existing Pharmacy Institutes having valid PCI
approval (& willing to continue with AICTE) to apply for Extension of Approval.
Q
Is it possible to get approval for New course in Emerging Area by reducing intake from 180
to 120 in Mechanical Course (without NBA)?
A
Yes. However, Institute needs to fulfil other conditions as per APH 2021-22 (Overall
enrolment greater than 50% & Nil Deficiency, NOC etc).
Q
What is the procedure for merging UG and PG courses running in same institute with one
college ID ?
A
UG courses can NOT be merged with PG courses. Merger allowed only at Respective Level.
Kindly Refer 2.18 of APH 2021-22.
Q
AICTE has made mandatory for the class 3 DSC, for 2 members. Whether the DSC should
be procured in the same name for both or separately as specified by AICTE.
A
DSCs should be procured as specified by AICTE, separately for each individual by position /
designation
Q
Whether a Standalone Architecture Institution approved by Council of Architecture, can be
merged with parent institution approved by AICTE.
Approval Process 2021-22
Frequently Asked Questions
Page | 25
A YES. If Architecture Institution is also having the approval of AICTE.
Q Please specify the eligibility conditions for grant of approval for ODL / OL courses.
A Please refer Chapter-5 of APH 2021-22
Q
UG engineering college having sanctioned intake of 300 with 5 courses. Whether New
course with intake 60 by reducing intake of two existing courses by 30 each can be added?
A Yes. Provided other conditions mentioned in APH are fulfilled.
Q Will there be any decision on awarding Autonomy for Polytechnics?
A Under consideration by AICTE
Q
Whether Institute can apply for three courses in Emerging Areas like Data Science, Artificial
Intelligence, IOT, Cybersecurity etc.
A
Yes. If the institute have at least three valid NBA Accredited courses and fulfilling other
conditions as mentioned in APH 2021-22.
Q Can we start diploma level course in areas other than Emerging /Multidisciplinary Areas?
A
In Engineering and Technology Program, the approval for any New Course at any Level shall
be ONLY in Emerging /Multidisciplinary Areas.
Q
Is the faculty to students ratio will be 1:20 for 2021-22 and 1:15 from 2022-23 for
Accredited and Autonomous Colleges.
A
AICTE institution should have FSR of 1:20 (UG Engineering & Technology). However,
Accredited and Autonomous institutions need to have 1:15 to maintain the quality education
Q
Please allow same courses at diploma & degree levels in engineering with total maximum
intake of 120 (Diploma + Degree) without any additional requirement of laboratories,
Workshop, Seminar hall and NBA.
A
Please Refer New Program /New Level Clause in Chapter-2 of APH 2021-22.
Q Can we go for restoration of intake of only few courses ?
A Yes
Approval Process 2021-22
Frequently Asked Questions
Page | 26
Q
Which Norms Architecture Colleges Should follow for taking AICTE Approval (Not
mentioned in APH 2020-21)?
A
Provision is made available on portal forthe Existing Architecture Colleges / Institutes having
valid COA approval (& willing to continue with AICTE) to apply for Extension of Approval.
Similarly, new Architecture Institute seeking AICTE Approval should have valid approval of
COA on the date of submission of application on AICTE Portal.
Q
AICTE granted approval for Vocational Courses last year, but State Government does not
publish it in their GR. Accordingly, the University NOT given affiliation to these Vocational
courses. So what is the status of these courses in 2021-22.
A
Institute may apply for grant of EOA from AICTE during the validity period of LOA. Also,
take up the issue with State Govt. to get it publish in State GR followed by affiliation from
the concerned affiliating University.
NOTE: AICTE has already requested all State Govt. & Technical Universities to look into the
issue.
Q Can we apply for New Course in existing Diploma college within Maximum Allowed Intake?
A Yes, if the institute fulfils conditions laid down in APH 2021-22.
Q
Mechanical Engineering course is Accredited by NBA is having 180 Intake now. Isit possible
to start new course in Emerging Area by reducing the intake from 180 to 120 in Mechanical
Engineering?
A Yes, if institute fulfils conditions laid down in APH 2021-22
Q
Whether reducing seats in MCA and MBA can be used for additional courses in B. Tech
Program?
A No. MBA and MCA are different Programs.
Q
Earlier Physics and mathematics were mandatory subjects in 10+2 level to take admission to
Engineering. Are these subjects NOT mandatory from 2021-22?
A
Please refer the APH 2021-22. Concerned State Authorities / Universities will decide on the
eligibility criteria for admission to Engineering courses.
NOTE: Please read AICTE Press Release on this subject matter (Dated 12-03-2021)
Q
Can Autonomous and Non-autonomous Institutions under the same TRUST in the same city
can be merged ?
Approval Process 2021-22
Frequently Asked Questions
Page | 27
A
Yes.
NOTE: Affiliating University will decide regarding Continuation of Autonomous Status after
merger.
Q
Whether Institute can Increase the intake more than last academic year 2020 -21by applying
for new courses in the Emerging Areas in this academic year 2021-22
A
No (Without NBA Accredited Courses Not possible). However, Institute can apply for New
Course in Emerging Area by reducing the intake in Existing Courses & fulfilling other
conditions of APH 2021-22.
Q
What is the TER Charges for reinstatement (Restoration) of seat from 30 to 60?
A Kindly refer APH 2021-22
Q
Within the total intake of the institute, can we reduce the intake in any one of the UG course
and increase the intake (using reduced one) in another UG program. Is it Possible ?
A NO
Q
During 2010 when AICTE made online provisionsfor EOA, our clerical staff wrongly entered
land area. Now how to correct it (land details not editable for institutes to change).
A
Please write to AICTE HQ through your Regional Office regarding your issue with supporting
documents. For more information, please Refer APH 2021-22.
Q
Can we adjust 180 seats in Emerging Areas by reducing intake of 180 through closure of
course/ reduction in course keeping the intake as intact?
A Emerging Area course is limited to one with 30 / 60 Intake.
Q
Is it possible to merge Diploma Institution into Degree Institution under same trust or
Society?
A Yes. Refer APH 2021-22 for other conditions.
Q
Our institute is under Extended EoA, shall we require to apply for EoA annually. As per APH
2021-22, in which category we should apply (EOA based on self-disclosure or Extended EoA)
?
A EoA based on self-disclosure.
Approval Process 2021-22
Frequently Asked Questions
Page | 28
Q
We have closed our MCA Course During 2012-13. Now We wish to Offer MCA Course
from the Academic Year 2021-22. Shall we need to apply as New Institutions or Existing
Institution.
A
As a New Institute. However, Existing Institutes can also start MCA as a New Program by
full filling the conditions of APH 2021-22.
Q
When will inspection for Merger of Institutions take place (after shifting the facilities from
child institution to parent institution or before)?
Q
In case of merger, kindly clarify whether facilities such as labs equipment need to be shifted
from child to parent institute before EVC visit or after approval it has to be shifted?
A
EVC will take place only after Scrutiny. Refer APH 2021-22. EVC will check for all the
facilities required to run the courses after merger as per the outcome of SC/Re-SC.
Q
The Nomenclature of PGDM Part Time and Executive PGDM programme is NOT available in
nomenclature list.
A
No Part Time Courses allowed. Now all the courses need to be conducted in Regular mode
or in Online / ODL mode.
Q Do we require approval from CoA for diploma in Architecture?
A
Approval of Council of Architect (COA) is essential for Architecture courses.
Q What is the Student Faculty Ratio for MBA programme?
A Refer APH 2021-22
Q
If there is a break in EOA for MBA program for more than six years and IF it is a State
University and MCA Department has AICTE approval. what is the procedure for getting
AICTE approval for MBA program?
A
University department has to apply as a New Program along with MCA (under the same
PID).
Q
Want to start standalone PGDM college using extra land with us. The land is in the name of
society but building plan in the name of existing college. Can we need building plan in the
name of new Institute.
A
If the existing land and building as required as per the APH 2021-22 for the Standalone
Institution with proper demarcation. Otherwise, not permissible. Ref APH 2021-22 for
more details
Approval Process 2021-22
Frequently Asked Questions
Page | 29
Q
What is the eligibility criteria for standalone ODL Institutes to apply for EOA for AY 2021-
22
A Kindly refer Chapter 5 of APH 2021-22
Q Can a Pharmacy Institute approved by PCI apply for EoA from AICTE?
A Yes.
Q
For Category I & II Autonomous Institutions (DUs) for starting new programs or increasing
the seats is NBA accreditation compulsory.
A Refer Chapter 4 of APH 2021-22
Q Can we start new program MCA in existing engineering institutes having already 300 seats
A YES
Q
UG Engineering College having sanctioned intake of 300 with 5 courses. Can we add new
course with intake 60 by reducing intake of two existing courses by 30 each?
A YES
Q Is the TER Charges applicable for reinstatement (restoration) of seats from 30 to 60
A Yes, if reduction is due to punitive action. Refer APH 2021-22 for more details.
Q Is an PGDM institute get additional 60 seats for this year 2021-22, without NBA
A No (if already having 300 intake). Refer APH 2021-22
Q
Is it possible to modify land details? Because the current land norm is less than that was
required at the time of starting of the college. Please allow to modify, so that we can use
Excess Land.
A
No. However permission will be given to use surplus land to run other educational
institutions (not for coaching / tuition centres, etc.). Refer Chapter -7 of APH 2021-22
Q
We are having total intake of 240.we would like to restore the seat of Electrical Branch from
30 to 60.which documents are required? what is the difference between the reinstatement
and restoration of seats.
Approval Process 2021-22
Frequently Asked Questions
Page | 30
A
For documents refer Appendix 17. Re-instatement is used normally to bring back the
reduced intake to original value (Reduced by the institute itself). Restoration normally used
to bring back the reduced intake to original intake (reduced by AICTE due to punitive action).
Q Whether institute can apply for Emerging Area Course by closing the Exiting course?
A Yes. As per the procedure laid down in APH 2021-22
Q
To start MCA in an existing aided college, Is AICTE approval should be taken first or
University Approval?
A AICTE approval. However NOC from affiliating University isrequired at the time of scrutiny.
Q
This year, in the Nomenclature list, a few courses (19 out of 261) are marked with star (*)
mark, indicating these courses as Emerging / Multi-disciplinary areas. Does it mean, we
can choose for new courses only from these 19 courses?
A YES
Q
We have only traditional courses in B.E. Level and got less admission i.e. less than 50 %
hence we like to reduce 60 seats of a traditional course from 120 seats to offer Emerging
course with 60 seats. Hence request you to relax the condition of minimum 50 % admission
last year given as Note in page no.55 of APH 2021-22 in Clause 2.14.4 (b) for effective
utilization of infrastructure.
A
Not possible. First reduce the intake and improve the enrolment/admissions through quality
education.
Q
Regarding New Course addition, our college has four accredited NBA course, without
changing the overall intake of the college, shall we reduce one division in existing course.
and shall we able to start new course in Emerging field but available as listed in Emerging
Area course list specified in AICTE Handbook 2021-22
A YES
Q Can we transfer the seats from one course to the other, like 30 seats from MBA(IT) to MCA?
A No. But reduction in MBA IT is allowed.
Q Institution having Autonomous status can apply for grant of approval for ODL
Approval Process 2021-22
Frequently Asked Questions
Page | 31
A No. Affiliated institutes are not allowed. Refer Chapter 5 of APH 2021-22.
Q
We reduced intake last year in Civil Mech. and ECE. Are we eligible to apply for additional
courses in Emerging areas like Artificial intelligence, Data science etc. without NBA?
A
Yes (by reducing seats in some courses / closing some courses), provided enrolment in AY
2019-20 should be more than 50%
Q Can we apply for two Management Courses in New College?
A Yes, as per the conditions mentioned in APH 2021-22.
Q
For Merger of Institution, who has to apply? Is it the Parent Institution or the Child
Institution?
A Parent Institution (Preferably).
Q Is it mandatory to get the approval from COA for Diploma in Architecture course?
A YES
Q
What is the procedure to Reduce the Land area? We having enough Land as per norms, is it
possible to reduce it sir
A
Land Area can’t be reduced. However NOC will be issued to eligible institutes for the use of
excess land for running other educational Institutions.
Q We want to reduce our B. Tech EEE course intake from 60 to 0.
A
Please apply on portal. Refer Appendix 17 APH 2021-22 for documents required to be
submitted.
Q
Can we Increase intake of course from 30 to 60 without NBA? (Our sanctioned intake is
more than 300, old Polytechnic & running 7 courses).
A NO
Q
We are a NAAC accredited MBA Institute affiliated to the University of Mumbai. If we wish
to start MBA (IEV) which is one of the Emerging areas, Is it must for us to have NBA
accreditation?
A Yes. Please refer Chapter-2 of APH 2021-22 for More details.
Approval Process 2021-22
Frequently Asked Questions
Page | 32
Q
We are Autonomous and have NAAC accreditation A+ grade till 2022 pl clarify whether
our TER charges will be waived in case of Extended EOA
A
Autonomous Institutes are eligible for Extended EOA. TER Charges will be waived OFF Only
for the eligible institutions as per the provisions of APH 2021-22.
Q Can we open a new course within approved sanctioned intake without NBA?
A Yes, in Emerging area as per APH 2021-22
Q
Emerging Area courses introduced last year (CSE-AI, CSE-AIML) will continue this year in
addition to * marked course in this year?
A
Only those courses approved last year and marked with * in this year’s approval process
handbook.
Q
We are an Autonomous Institution, want to apply for ME Programme in CSE (AI&ML) but
this Programme is not offered by the affiliating university Anna University, Can AICTE will
permit us to start the Programme.
A NO. It is mandatory to have University NOC plus 50% enrolment.''')

# with open('data.txt', 'r') as file:
#     data = file.read().replace('\n', '')
#
# ans = nlp(data)

# [{'answer': '42', 'question': 'What is the answer to life, the universe and everything?'}]
print(ans)

anslist = []
quelist = []
for qa in ans:
    anslist.append(qa.get('answer'))
    quelist.append(qa.get('question'))

print("OUR list is: ")
print(anslist, quelist)

iterate = 0
for intent in intentsfile['intents']:
    for answer in anslist:
        list = []
        intent['tag'] = f"Data-{str(iterate + 1)}"
        list.append(quelist[iterate])
        intent['patterns'] = list
        list = []
        list.append(answer)
        intent['responses'] =  list

        iterate +=1

        # for question in quelist:
        #     intent['patterns'] = question
        #     break
        # intent.udpate('tag') = "index"
        updatejson(intent)

lastupdateTag()


# for intent in intentsfile['intents']:
#     for question in quelist:
#         # intent.udpate('tag') = "index"
#         updatejson(intent)




#
# for intent in intentsfile['intents']:
#     # ques = updatePatterns(intent.get('patterns')[0])
#     # for i in ques:
#     #     print(i)
#     #     intent.get('patterns').append(i)
#     print(intent.get('patterns'))
#     updatejson(intent)
#     print('done')



# print(f"ans is {ans[0].get('answer')}")
# print(f"Que  is {ans[0].get('question')}")
# for qa pass a dict with "question" and "context"
# nlp({
#     "question": "What is 42 ?",
#     "context": "42 is the answer to life, the universe and everythi\
#     ng."
# })
# 'the answer to life, the universe and everything'
