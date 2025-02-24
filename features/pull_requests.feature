Feature: Repository interaction

  Scenario Outline: Retrieve repositories
      Given the repository of "<repo>"
      When we use the core library to query for all pull requests
      Then the response should not be None or empty

      Examples: Personal repositories
        | repo                                        |
        | benjaminlukeclark/Get-Duplicate-Files       |
        | benjaminlukeclark/PowerShell-Intro-Training |
        | othneildrew/Best-README-Template            |

      Examples: Organisational Repositories
        | repo                                            |
        | sudoblark/sudoblark.terraform.github            |
        | sudoblark/sudoblark.python.core                 |
        | sudoblark/sudoblark.terraform.modularised-demo  |