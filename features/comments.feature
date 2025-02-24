Feature: Comment interaction

  Scenario Outline: Create and update comments
      Given that we are testing for comment interactions
      When we have the content of "<body>"
      Then we should be able to "<operation>" a comment

      Examples: Create some comments
        | body            | operation |
        | Test comment 1  | post      |
        | Test comment 2  | post      |
        | Test comment 3  | post      |


      Examples: Update some comments
        | body      | operation |
        | Update 1  | post      |
        | Update 2  | post      |
        | Update 3  | post      |

      Examples: Overwrite some comments
        | body  | operation      |
        | 1     | overwrite      |
        | 2     | overwrite      |
        | 3     | overwrite      |

  Scenario: Delete a comment
      Given that we are testing for comment interactions
      Then we should be able to delete a comment