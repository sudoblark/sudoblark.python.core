Feature: Organisation interaction

  Scenario Outline: Retrieve organisations
      Given the organisation of "<org>"
      When we use the core library to query the organisation
      Then the response should not be None or empty

      Examples: Organisations
        | org       |
        | sudoblark |
        | adobe     |
        | netflix   |