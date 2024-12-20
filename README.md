## Description

The Stock Market Analysis System is a Django application that allows you to execute positions based on specific market conditions, using financial asset data, indicators, and machine learning models.

## Features

- Trend analysis based on the last 5 market movements.
- Utilization of three main indicators:
  - SMA 50 (Simple Moving Average over 50 periods)
  - SMA 10 (Simple Moving Average over 10 periods)
  - RSI (Relative Strength Index)
- Management of session reports sent by SMTP
  - Weekly divided into days and session type.
- Implementation of hexagonal as base architecture.
  - Handlers (Presentations)
  - Services (Business Logic)
  - Entities (Persistence)
- Implementation of Unitest (TDD)
  - Services (Business Logic)
  - Entities (Persistence)
- Machine model (Logistic regression)
  - Creation
  - Training
  - Evaluation (Implementation of confusion matrices)
  - Predictions
  - Persistence in training and persistence
 
## Technologies Used

- **Programming Language**: Python
- **Framework**: Django
- **Libraries**:
  - Pandas (for data handling)
  - Scikit-learn (for Machine Learning models)
  - NumPy (for numerical operations)
  - Django Rest Framework (for building APIs)
  - TestCase (for unit testing the API and machine learning predictions)
  - Pickle (for saving and loading the machine learning models)
  - Decouple (for environment variable management)
  - Seaborn (for data visualization)
  - Matplotlib (for plotting graphs and charts)
- **Data Format**: JSON
- **Database**: Mysql (To give traceability to the positions)
- **Machine Learning Model**: Stored in `.pkl` file
- **Containerization**: Docker (used for packaging and deploying the application in a consistent environment)

## Usage

To use the system, follow these steps:

1. **Trend Analysis:**
   - Observe trends based on the last 5 market movements.

2. **Available Indicators:**
   - Use SMA 50, SMA 10, and RSI indicators to make informed decisions on your positions.

3. **Machine Learning:**
   - Use General Logístic Regression Model to make informed decisions on your positions.
     
4. **Management Reports:**
   - Schedule the sending of session reports by email.

## Installation

### Prerequisites

Make sure you have Python and Django installed in your development environment.

### Installation Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/danielsuniaga/samb.git
   cd your-repository
