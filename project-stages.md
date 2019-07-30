## I. Overview
This governance policy describes how an open source project can formally join LF Energy via the [Project Proposal Process](). It describes the [Stages]() a project may be admitted under and what the criteria and expectations are for a given stage, as well as the acceptance criteria for a project to move from one stage to another. It also describes the [Annual Review Process]() through which those changes will be evaluated and made. 

Project progression - movement from one stage to another - allows projects to participate at the level that is most appropriate for them given where they are in their lifecycle. Regardless of stage, all LF Energy projects benefit from a deepened alignment with existing projects, and access to mentorship, support, and foundation resources.

For more information about how your project can benefit from LF Energy membership and services, please see [TBD Document]().


## II. Project Proposal Process

### Introduction
This governance policy sets forth the proposal process for projects to be accepted into LF Energy. The process is the same for both existing projects which seek to move into LF Energy and new projects to be formed within LF Energy.

### Project Proposal Requirements
Projects must be formally proposed via GitHub. Project proposals submitted to LF Energy should provide the following information to the best of their ability:

* name of project
* project description (what it does, why it is valuable, origin and history)
* statement on alignment with the mission in the LF Energy charter
* link to *current* Code of Conduct (if one is adopted already)
* sponsor from TAC, if identified (a sponsor helps mentor projects)
* project license 
* source control (GitHub by default)
* issue tracker (GitHub by default)
* external dependencies, including licenses
* release methodology and mechanics
* names of initial committers, if different from those submitting proposal
* briefly describe the project's leadership team and decision-making process
* link to any documented governance practices
* preferred maturity level (see stages below)
* list of project's official communication channels (slack, irc, mailing lists)
* link to project's website 
* links to social media accounts
* existing financial sponsorship
* infrastructure needs or requests 

### Project Acceptance Process
* Projects are required to present their proposal at a TAC meeting
* The TAC may ask for changes to bring the project into better alignment with LF Energy (adding a governance document to a repository or adopting a Code of Conduct, for example).
 * The project will need to make these changes in order to progress further.
* Projects are accepted via a 2/3 supermajority vote of the TAC.
* The proposal document will be finalized as a project charter. This charter document must be included in the project's main repository.
* The TAC will determine the appropriate initial stage for the project. The project can apply for a different stage via the review process. 

## III. Stages - Definitions & Expectations
Every LF Energy project has an associated maturity level. Proposed projects should state their preferred maturity level.

All projects may attend TAC meetings and contribute work regardless of their stage. 


### Sandbox Projects
**Definition** 

Sandbox projects are projects which the TAC believes are, or have the potential to be, important to the ecosystem of Projects or ecosystem as a whole. They may be early-stage projects just getting started, or they may be long-established projects with minimal resource needs. The Sandbox stage provides a beneficial, neutral home for these projects in order to foster collaborative development and provide a path to deeper alignment with other LF Energy projects via the graduation process.

**Examples**

1. New projects that are designed to extend one or more LF Energy projects with functionality or interoperability libraries. 
1. Independent projects that fit within the LF Energy mission and provide potential for a novel approach to existing functional areas (or are an attempt to meet an unfulfilled need).
1. Projects commissioned or sanctioned by LF Energy.
1. Any project that realistically intends to join LF Energy Incubating or Graduated Stages in the future and wishes to lay the foundations for that transition.

**Expectations**

End users should evaluate Sandbox projects with care, as this stage does not set requirements for community size, governance, or production readiness. Sandbox projects will receive minimal support from the LF Energy. Projects will be reviewed on an annual basis; they may also request a status review by submitting a report to the TAC.

**Acceptance Criteria**

To be considered for the Sandbox Stage, the project must meet the following requirements:
* 2 TAC sponsors to champion the project & provide mentorship as needed
* A presentation at the meeting of the TAC
* Adherence to LF Energy’s IP Policy
* Adoption of LF Energy Code of Conduct
* Operating TSC with at least 3 members, one chair elected or appointed by sponsoring organization or LF Energy
* Final acceptance by TAC, 2/3 majority
* Upon acceptance, Sandbox projects must list and maintain their status prominently on their website/README

### Incubator Stage
**Definition** 

The Incubator Stage is for projects that are interested in reaching the Graduated Stage, and have identified a growth plan for doing so. Incubator Stage projects will receive mentorship from the TAC and are expected to actively develop their community of contributors, governance, project documentation, and other variables identified in the growth plan that factor in to broad success and adoption.

In order to support their active development, projects in the Incubator stage have a higher level of access to foundation resources, which will be agreed upon and reviewed on a yearly basis. A project's progress toward its growth plan goals will be reviewed on a yearly basis, and the TAC may ask the project to move to the Sandbox stage if progress on the plan drops off or stalls. 

**Examples**

1. Projects that are on their way or very likely to mature to Graduated status.
1. Projects that have developed new growth targets or other community metrics for success.
1. Projects that are looking to create a lifecycle plan (maintainership succession, contributor programs, version planning, etc.)
1. Projects that need more active support from LF Energy Governing Board or TAC mentorship in order to reach their goals. 

**Expectations**

Projects in the Incubating stage are generally expected to move to the Graduated stage within two years. Depending on their growth plans, projects may cycle through Sandbox, Incubating, or Graduated stage as needed.  

**Acceptance Criteria**

To be considered for Incubating Stage, the project must meet the Sandbox requirements as well as the following:

 * Development of a growth plan, to be done in conjunction with their project mentor(s) at the TAC.
 * Document that it is being used successfully in production by at least two independent end users which, in the TAC’s judgement, are of adequate quality and scope.
 * Demonstrate a substantial ongoing flow of commits and merged contributions.
 * Demonstrate that the current level of community participation is sufficient to meet the goals outlined in the growth plan.
 * Since these metrics can vary significantly depending on the type, scope and size of a project, the TAC has final judgement over the level of activity that is adequate to meet these criteria.
 * Operating TSC with at least 5 members and a chair elected by the members
 * Explicitly define a project governance and committer process. This is preferably laid out in a GOVERNANCE.md file and references a CONTRIBUTING.md and OWNERS.md file showing the current and emeritus committers.
 * Other metrics as defined by the applying Project during the application process in cooperation with the TAC.
 * Receive a two-thirds supermajority vote of the TAC to move to Incubating Stage. 

### Graduated Stage
**Definition**

The Graduated Stage is for projects that have reached their growth goals and are now on a sustaining cycle of development, maintenance, and long-term support. Graduated Stage projects are used commonly in enterprise production environments and have large, well-established project communities.     

**Examples**

1. Projects that have publicly documented release cycles and plans for Long Term Support ("LTS").
1. Projects that have themselves become platforms for other projects.
1. Projects that are able to attract a healthy number of committers on the basis of its production usefulness (not simply 'developer popularity').
1. Projects that have several, high-profile or well known end-user implementations.

**Expectations**

Graduated Stage projects are expected to participate actively in TAC proceedings, and as such have a binding vote on TAC matters requiring a formal vote, such as the election of a TAC representative. They receive ongoing financial and marketing support from LF Energy, and are expected to cross promote the foundation along with their activities.

**Acceptance Criteria**

To graduate from Sandbox or Incubator status, or for a new project to join with Graduated status, a project must meet the Incubator stage criteria plus:

 * Have a defined governing body of at least 5 or more members (owners and core maintainers), of which no more than 1/3 is affiliated with the same employer. In the case there are 5 governing members, 2 may be from the same employer. 
 * Have a documented and publicly accessible description of the project's governance, decision-making, and release processes.
 * Have a healthy number of maintainers from at least two organizations. A maintainer or committer is defined as someone with the commit bit; i.e., someone who can accept contributions to some or all of the project.
 * Have a public list of project adopters for at least the primary repo (e.g., ADOPTERS.md or logos on the project website).
 * Receive a supermajority vote from the TAC to move to Graduated stage. Projects can move directly from Sandbox to Graduated status if they can demonstrate sufficient maturity and have met all requirements. 


### Emeritus Stage
**Definition**

Emeritus projects are projects which the maintainers feel have reached or are nearing end-of-life. Emeritus projects have contributed to the ecosystem, but are not necessarily recommended for modern development as there may be more actively maintained choices. LF Energy appreciates the contributions of these projects and their communities, and the role they have played in moving the ecosystem forward. 

**Examples**

1. Projects that are "complete" by the maintainers' standards.
1. Projects that do not plan to release major versions in the future.

**Expectations**

Projects in this stage are not in active development. Their maintainers may infrequently monitor their repositories, and may only push updates to address security issues, if at all. Emeritus projects should clearly state their status and what any user or contributor should expect in terms of response or support. If there is an alternative project the maintainers recommend, it should be listed as well. The foundation will continue to hold the IP and any trademarks and domains, but the project does not draw on foundation resources. 

**Acceptance Criteria**

Projects may be granted Emeritus status via a 2/3 vote from the TAC and with approval from project ownership. In cases where there is a lack of project ownership, only a 2/3 vote from the TAC is required.


## IV. Annual Review Process

The TAC shall develop an annual review process to determine whether projects are in the stage that accurately reflects their needs and goals. 
