## story_1              
* greet              
  - utter_greet
* query_days_in_month{"month": "january"}
  - utter_answer_31_days
* query_days_in_month{"month": "february"}
  - utter_answer_28_days
* query_days_in_month{"month": "april"}
  - utter_answer_30_days
* query_days_in_month{"month": "march"}
  - utter_answer_31_days
* get_joke
  - action_joke
* bye
  - utter_bye

## story_2
* greet
    - utter_greet
* query_days_in_month{"month": "june"}
    - utter_answer_30_days
* get_joke
    - action_joke
* bye
    - utter_bye

## story_3
* greet
    - utter_greet
* get_joke
    - action_joke
* get_joke
    - action_joke
* get_joke
    - action_joke
* bye
    - utter_bye
    
## story_4
* greet
    - utter_greet
* query_days_in_month{"month": "march"}
    - utter_answer_31_days
* get_joke
    - action_joke
* query_days_in_month{"month": "january"}
    - utter_answer_31_days
* get_joke
    - action_joke
* bye
    - utter_bye