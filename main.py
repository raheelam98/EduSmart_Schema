# edu_smart_schema - main.py

from pydantic import Field
from datetime import date

from pydantic import BaseModel
from typing import List, Optional
import uuid
from enum import Enum

# Define class models using Pydantic to represent the structure of nodes

class ProgramModel(BaseModel):
    program_id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()), nullable=False, primary_key=True)
    name: str = Field(nullable=False)
    description: str

class CourseModel(BaseModel):
    course_id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()), nullable=False, primary_key=True)
    course_number: str = Field(nullable=False)
    name: str = Field(nullable=False)
    description: str

class SectionModel(BaseModel):
    section_number: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()), nullable=False, primary_key=True)
    start_date: str = Field(default=date.today())
    end_date: str = Field(default=date.today())
    class_days_of_week: str = Field(nullable=False)
    class_time: str = Field(nullable=False)
    class_duration: int = Field(nullable=False)
    lab_days_of_week: str = Field(nullable=False)
    lab_time: str = Field(nullable=False)
    lab_duration: int = Field(nullable=False)

class PersonModel(BaseModel):
    person_id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()), nullable=False)
    name: str = Field(nullable=False)
    photo_url: Optional[str]
    givenName: str = Field(nullable=False)
    familyName: str = Field(nullable=False)
    birthDate: str = Field(default_factory=lambda: date.today().isoformat())
    signupDate: str = Field(default_factory=lambda: date.today().isoformat())

class TeacherModel(PersonModel):
    teacher_id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()), nullable=False)

class StudentModel(PersonModel):
    student_id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()), nullable=False, primary_key=True)
    roll_no: str = Field(nullable=False)

class ProfileModel(BaseModel):
    education_level: str = Field(nullable=False)
    work_experience: Optional[str]
    english_reflections: Optional[str]
    iq_reflection: Optional[str]
    learning_style: Optional[str]
    current_level: str
    last_updated: str = Field(default=date.today())

class SkillModel(BaseModel):
    skill_id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()), nullable=False, primary_key=True)
    name: str = Field(nullable=False)
    description: Optional[str]
    category: Optional[str]
    proficiency_level: str
    last_assessed: Optional[str] = Field(default=date.today())
    access_source: Optional[str]
    reflections: Optional[str]

class TextBookModel(BaseModel):
    textbook_id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()), nullable=False, primary_key=True)
    title: str = Field(nullable=False)
    author_name: str = Field(nullable=False)
    description: Optional[str]

class TopicModel(BaseModel):
    topic_id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()), nullable=False, primary_key=True)
    title: str = Field(nullable=False)
    url: Optional[str]
    details: Optional[str]
    topic_level: Optional[int]
    last_reviewed: str = Field(default=date.today())
    creation_date: str = Field(default=date.today())
    sequence_number: int = Field(nullable=False)    

class TopicContentModel(BaseModel):
    id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()), nullable=False, primary_key=True)
    content: str  ## check
    embeddings: Optional[any]
    last_updated: str = Field(default=date.today())   
    
class CompletedTopicModel(BaseModel):
    level: int = Field(nullable=False)
    assessment_date: str = Field(default=date.today())

## QuestionBank Questions and Answers Related to Topics (CaseStudy is Skipped for Time)

class QuestionModel(BaseModel):
    question_id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()), nullable=False, primary_key=True)
    question_text: str = Field(nullable=False)
    difficulty_level: Optional[str]
    points: int = Field(nullable=False)

class FreeTextModel(QuestionModel):
    reference_answer: str = Field(nullable=False)

class CodingModel(QuestionModel):
    ideal_answer: str = Field(nullable=False)

class SingleSelectModel(QuestionModel):
    pass

class MultiSelectModel(QuestionModel):
    pass

class OptionModel(BaseModel):
    option_id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()), nullable=False, primary_key=True)
    answer_text: str = Field(nullable=False)
    is_correct: bool = Field(nullable=False)  

## QuestionBank Questions and Answers Related to Topics (CaseStudy is Skipped for Time)

class QuestionModel(BaseModel):
    question_id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()), nullable=False, primary_key=True)
    question_text: str = Field(nullable=False)
    difficulty_level: Optional[str]
    points: int = Field(nullable=False)

class FreeTextModel(QuestionModel):
    reference_answer: str = Field(nullable=False)

class CodingModel(QuestionModel):
    ideal_answer: str = Field(nullable=False)

class SingleSelectModel(QuestionModel):
    pass

class MultiSelectModel(QuestionModel):
    pass

class OptionModel(BaseModel):
    option_id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()), nullable=False, primary_key=True)
    answer_text: str = Field(nullable=False)
    is_correct: bool = Field(nullable=False)     

# Interaction Nodes and Student Assessment Tracking
# Use-Case:
#   2. AfterTopic/s // (Interaction)    

class InteractionModel(BaseModel):
    interaction_id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()), nullable=False, primary_key=True)
    total_questions: Optional[int]
    creation_date: str = Field(default=date.today())
    end_date: Optional[str] = Field(default=date.today())

class StatusEnum(str, Enum):
    assigned = 'assigned'
    in_progress = 'in_progress'
    completed = 'completed'

class StudentInteractionModel(BaseModel):
    student_interaction_id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()), nullable=False, primary_key=True)
    status: StatusEnum = Field(nullable=False)
    assigned_date: str = Field(default=date.today())
    start_date: Optional[str] = Field(default=date.today())
    last_updated: Optional[str] = Field(default=date.today())
    percentage: Optional[float]
    score: Optional[int]

class LearningExchangeModel(BaseModel):
    exchange_id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()), nullable=False, primary_key=True)
    student_response: str = Field(nullable=False)
    is_correct: Optional[bool]
    needs_reinforcement: Optional[bool]
    exchange_timestamp: str = Field(default=date.today())
    sequence_number: int = Field(nullable=False)
    feedback: Optional[str]

#   1. Assessment (This can be Quiz or Assessment)
    
class AssessmentModel(BaseModel):
    id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()), nullable=False, primary_key=True)
    title: Optional[str]
    details: Optional[str]
    passing_score: Optional[int]

class AssignmentProjectModel(BaseModel):
    id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()), nullable=False, primary_key=True)
    title: str
    details: Optional[str]
    passing_score: Optional[int]
    max_duration: Optional[int]     

class QuizModel(BaseModel):
    id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()), nullable=False, primary_key=True)
    title: Optional[str]
    total_questions: Optional[int]
    max_score: Optional[int]
    time_duration: Optional[int]
    topics_count: Optional[int]

class AnswerSheetModel(BaseModel):
    id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()), nullable=False, primary_key=True)
    question_ids: List[any]
    grade: Optional[float]
    start_time: str = Field(default=date.today())
    end_time: str = Field(default=date.today())

class AttemptedAnswerModel(BaseModel):
    id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()), nullable=False, primary_key=True)
    question: str
    answer: str
    score: Optional[float] 

class OnlineSessionScheduleModel(BaseModel):
    id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()), nullable=False, primary_key=True)
    zoom_link: Optional[str]
    topics_to_cover: List[str]
    class_time: str = Field(default=date.today())
    class_day: str
    class_status: Optional[bool]

class NotificationModel(BaseModel):
    id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()), nullable=False, primary_key=True)
    content: str
    notification_time: str = Field(default=date.today())
          
## ============================  *** ============================ ##
## ============================  *** ============================ ##  

# create a function to add nodes and relationships to the database using these models

from py2neo import Graph, Node, Relationship

# Connect to the Neo4j database
graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))

# Function to create a Program node
def create_program_node(program: ProgramModel):
    program_node = Node("Program", **program.dict())
    graph.create(program_node)
    return program_node

# Function to create a Course node and its relationship with Program
def create_course_node(course: CourseModel, program_node: Node):
    course_node = Node("Course", **course.dict())
    includes_rel = Relationship(program_node, "INCLUDES", course_node)
    graph.create(course_node)
    graph.create(includes_rel)
    return course_node

# Function to create a Section node and its relationship with Course
def create_section_node(section: SectionModel, course_node: Node):
    section_node = Node("Section", **section.dict())
    scheduled_rel = Relationship(course_node, "SCHEDULED", section_node)
    graph.create(section_node)
    graph.create(scheduled_rel)
    return section_node

def create_person_node(person: PersonModel):
    person_node = Node("Person", **person.dict())
    graph.create(person_node)
    return person_node

def create_student_node(student: StudentModel, program_node: Node ):
    student_node = Node("Student", **student.dict())
    graph.create(student_node)
    take_admission_rel = Relationship(student_node, "TAKE_ADMISSION", program_node)
    graph.create(take_admission_rel)    
    return student_node

def create_profile_node(profile: ProfileModel, student_node: Node):
    profile_node = Node("Profile", **profile.dict())
    graph.create(profile_node)
    has_profile_rel = Relationship(student_node, "HAS_PROFILE", profile_node)
    graph.create(has_profile_rel)
    return profile_node

def create_skill_node(skill: SkillModel, profile_node: Node):
    skill_node = Node("Skill", **skill.dict())
    graph.create(skill_node)
    has_skill_rel = Relationship(profile_node, "HAS_SKILL", skill_node, proficiency=skill.proficiency_level, date_acquired=skill.last_assessed)
    graph.create(has_skill_rel)
    return skill_node

def create_teacher_node(teacher: TeacherModel, section_node: Node, assessment_node: Node, topic_node: Node):
    teacher_node = Node("Teacher", **teacher.dict())
    graph.create(teacher_node)
    teaches_rel = Relationship(teacher_node, "TEACHES", section_node)
    manages_assessment_rel = Relationship(teacher_node, "MANAGES_ASSESSMENT", assessment_node)
    manages_topic_rel = Relationship(teacher_node, "MANAGES_TOPIC", topic_node)
    graph.create(teaches_rel)
    graph.create(manages_assessment_rel)
    graph.create(manages_topic_rel)
    return teacher_node

def create_textbook_node(textbook: TextBookModel, course_node: Node):
    textbook_node = Node("TextBook", **textbook.dict())
    graph.create(textbook_node)
    has_required_textbook_rel = Relationship(course_node, "HAS_REQUIRED_TEXTBOOK", textbook_node)
    graph.create(has_required_textbook_rel)
    return textbook_node

def create_topic_node(topic: TopicModel, textbook_node: Node):
    topic_node = Node("Topic", **topic.dict())
    graph.create(topic_node)
    covers_rel = Relationship(textbook_node, "COVERS", topic_node)
    graph.create(covers_rel)
    return topic_node

#  DIRECTED EDGE CONTAINS_TOPIC CONNECTING (Topic -> Topic)

def create_topic_relationships(topic_node: Node, related_topic_node: Node):
    contains_topic_rel = Relationship(topic_node, "CONTAINS_TOPIC", related_topic_node)
    graph.create(contains_topic_rel)

# Function to create TopicContent node
def create_topic_content_node(topic_content: TopicContentModel, topic_node: Node):
    topic_content_node = Node("TopicContent", **topic_content.dict())
    graph.create(topic_content_node)
    contains_content_rel = Relationship(topic_node, "CONTAINS_CONTENT", topic_content_node)
    graph.create(contains_content_rel)
    return topic_content_node

# Function to create CompletedTopic relationship 

def create_completed_topic_relationship(student_node: Node, topic_node: Node, completed_topic: CompletedTopicModel):
    completed_topic_rel = Relationship(student_node, "COMPLETED_TOPIC", topic_node, **completed_topic.dict())
    graph.create(completed_topic_rel)
    return completed_topic_rel

#  QuestionBank Questions and Answers Related to Topics (CaseStudy is Skipped for Time)

# UNDIRECTED EDGE CONTAINS {} CONNECTING (Topic ~ Question)   

def create_question_node(question : QuestionModel, topic_node : Node):
    question_node = Node("Question", **question.dict())
    graph.create(question_node)
    contains_rel = Relationship(topic_node, "CONTAINS", question_node)
    graph.create(contains_rel)
    return question_node

def create_free_text_node(free_text: FreeTextModel,  question_node: Node):
    free_text_node = Node("FreeText", **free_text.dict())
    graph.create(free_text_node)
    is_a_type_rel = Relationship(question_node, "IS_A_TYPE", free_text_node )
    graph.create(is_a_type_rel) 
    return free_text_node

def create_coding_node(coding: CodingModel, question_node: Node):
    coding_node = Node("Coding", **coding.dict())
    graph.create(coding_node)
    is_a_type_rel = Relationship(question_node, "IS_A_TYPE", coding_node )
    graph.create(is_a_type_rel) 
    return coding_node

def create_single_select_node(single_select: SingleSelectModel, question_node: Node):
    single_select_node = Node("SingleSelect", **single_select.dict())
    graph.create(single_select_node)
    is_a_type_rel = Relationship(question_node, "IS_A_TYPE", single_select_node )
    graph.create(is_a_type_rel) 
    return single_select_node

def create_multi_select_node(multi_select: MultiSelectModel, question_node: Node):
    multi_select_node = Node("MultiSelect", **multi_select.dict())
    graph.create(multi_select_node)
    is_a_type_rel = Relationship(question_node, "IS_A_TYPE", multi_select_node )
    graph.create(is_a_type_rel) 
    return multi_select_node

def create_option_node(option: OptionModel, question_node: Node):
    option_node = Node("Option", **option.dict())
    graph.create(option_node)
    if isinstance(question_node, SingleSelectModel):
        has_option_rel = Relationship(question_node, "HAS_SINGLE_OPTION", option_node)
    elif isinstance(question_node, MultiSelectModel):
        has_option_rel = Relationship(question_node, "HAS_MULTIPLE_OPTION", option_node)
    graph.create(has_option_rel)
    return option_node

# Interaction Nodes and Student Assessment Tracking
# Use-Case:

#   2. AfterTopic/s // (Interaction)   

def create_interaction_node(interaction: InteractionModel):
    interaction_node = Node("Interaction", **interaction.dict())
    graph.create(interaction_node)
    return interaction_node

def create_student_interaction_node(student_interaction: StudentInteractionModel, student_node: Node, interaction_node: Node):
    student_interaction_node = Node("StudentInteraction", **student_interaction.dict())
    graph.create(student_interaction_node)
    has_participation_rel = Relationship(student_node, "HAS_PARTICIPATION", student_interaction_node)
    assigned_to_interaction_rel = Relationship(student_interaction_node, "ASSIGNED_TO_INTERACTION", interaction_node)
    graph.create(has_participation_rel)
    graph.create(assigned_to_interaction_rel)
    return student_interaction_node

def create_learning_exchange_node(learning_exchange: LearningExchangeModel, student_interaction_node: Node, question_node: Node):
    learning_exchange_node = Node("LearningExchange", **learning_exchange.dict())
    graph.create(learning_exchange_node)
    includes_learning_exchange_rel = Relationship(student_interaction_node, "INCLUDES_LEARNING_EXCHANGE", learning_exchange_node)
    answered_question_rel = Relationship(learning_exchange_node, "ANSWERED_QUESTION", question_node)
    graph.create(includes_learning_exchange_rel)
    graph.create(answered_question_rel)
    return learning_exchange_node

#   1. Assessment (This can be Quiz or Assessment)

def create_assessment_node(assessment: AssessmentModel):
    assessment_node = Node("Assessment", **assessment.dict())
    graph.create(assessment_node)
    return assessment_node

def create_assignment_project_node(assignment_project: AssignmentProjectModel, assessment_node: Node):
    assignment_project_node = Node("Assignment_Project", **assignment_project.dict())
    graph.create(assignment_project_node)
    includes_project_rel = Relationship(assessment_node, "INCLUDES_PROJECT", assignment_project_node)
    graph.create(includes_project_rel)
    return assignment_project_node

def create_assessment_relationships(assessment_node: Node, quiz_node: Node, section_node: Node):
    has_quiz_rel = Relationship(assessment_node, "HAS_QUIZ", quiz_node)
    mandatory_assessment_for_rel = Relationship(assessment_node, "MANDATORY_ASSESSMENT_FOR", section_node, due_date=date.today().isoformat())
    graph.create(has_quiz_rel)
    graph.create(mandatory_assessment_for_rel)

def create_student_assessment_relationship(student_node: Node, assessment_node: Node, assessment_type: str):
    attempts_assessment_rel = Relationship(student_node, "ATTEMPTS_ASSESSMENT", assessment_node, assessment_type=assessment_type)
    graph.create(attempts_assessment_rel)

def create_quiz_node(quiz: QuizModel, course_node: CourseModel, topic_node: TopicModel):
    quiz_node = Node("Quiz", **quiz.dict())
    graph.create(quiz_node)
    belongs_to_rel = Relationship(quiz_node, "BELONGS_TO", course_node)
    covers_topic_rel = Relationship(quiz_node, "COVERS_TOPIC", topic_node)
    graph.create(belongs_to_rel)
    graph.create(covers_topic_rel)
    return quiz_node

def create_answer_sheet_node(answer_sheet: AnswerSheetModel, student_node: StudentModel, quiz_node: QuizModel):
    answer_sheet_node = Node("AnswerSheet", **answer_sheet.dict())
    graph.create(answer_sheet_node)
    has_attempt_rel = Relationship(student_node, "HAS_ATTEMPT", answer_sheet_node, attempt_date=date.today().isoformat(), submission_status="submitted")
    has_response_rel = Relationship(quiz_node, "HAS_RESPONSE", answer_sheet_node)
    graph.create(has_attempt_rel)
    graph.create(has_response_rel)
    return answer_sheet_node

## Right Now we don't have student attempted answers connected to Question. If this use case is required
##  We can create an Answers nodes connected AnswerSheet to Questions.

def create_attempted_answer_node(attempted_answer: AttemptedAnswerModel, answer_sheet_node: AnswerSheetModel, question_node: QuestionModel):
    attempted_answer_node = Node("AttemptedAnswer", **attempted_answer.dict())
    graph.create(attempted_answer_node)
    contains_attempted_answer_rel = Relationship(answer_sheet_node, "CONTAINS_ATTEMPTED_ANSWER", attempted_answer_node)
    is_response_to_question_rel = Relationship(attempted_answer_node, "IS_RESPONSE_TO_QUESTION", question_node)
    graph.create(contains_attempted_answer_rel)
    graph.create(is_response_to_question_rel)
    return attempted_answer_node

# // Classes & Tracking  

def create_online_session_schedule_node(online_session_schedule: OnlineSessionScheduleModel, section_node: SectionModel, course_node: CourseModel):
    online_session_schedule_node = Node("OnlineSessionSchedule", **online_session_schedule.dict())
    graph.create(online_session_schedule_node)
    has_section_schedule_rel = Relationship(section_node, "HAS_SECTION_SCHEDULE", online_session_schedule_node)
    graph.create(has_section_schedule_rel)
    has_course_schedule_rel = Relationship(course_node, "HAS_COURSE_SCHEDULE", online_session_schedule_node)
    graph.create(has_course_schedule_rel)
    for topic_title in online_session_schedule.topics_to_cover:
        topic_node = graph.nodes.match("Topic", title=topic_title).first()
        if topic_node:
            teaches_topic_rel = Relationship(online_session_schedule_node, "TEACHES_TOPIC", topic_node, date=date.today().isoformat())
            graph.create(teaches_topic_rel)
    return online_session_schedule_node

def create_notification_node(notification : NotificationModel, student_node: Node, teacher_node: Node, section_node: Node, course_node: Node ):
    notification_node = Node("Notification", **notification.dict())
    graph.create(notification_node)

    notifies_student_rel = Relationship(notification_node, "NOTIFIES_STUDENT", student_node)
    manages_notification_rel = Relationship(teacher_node, "MANAGES_NOTIFICATION", notification_node)
    notifies_section_rel = Relationship(notification_node, "NOTIFIES_SECTION", section_node)
    notifies_course_rel = Relationship(notification_node, "NOTIFIES_COURSE", course_node)

    graph.create(notifies_student_rel)
    graph.create(manages_notification_rel)
    graph.create(notifies_section_rel)
    graph.create(notifies_course_rel)
    return notification_node

## ============================  *** ============================ ##
## ============================  *** ============================ ##  
