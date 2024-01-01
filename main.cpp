#include "tradeEngine.h"

std::tuple<std::string, double, double> TradingEngine::monitorFile(const std::string& filename) {
    std::string companyName;
    double shortTermMA = 0.0;
    double longTermMA = 0.0;
    while (true) {
        std::ifstream file(filename);
        std::string currentLine;
        // needs refactoring to read all lines
        if (file) {
            std::cout << "Reading " << filename << std::endl;
            while (getline(file, currentLine)) {
                // Split the line into companyName, shortTermMA and longTermMA
                std::istringstream iss(currentLine);
                std::getline(iss, companyName, ',');
                std::string shortTermMAStr, longTermMAStr;
                std::getline(iss, shortTermMAStr, ',');
                std::getline(iss, longTermMAStr);
                shortTermMA = std::stod(shortTermMAStr);
                longTermMA = std::stod(longTermMAStr);
                return std::make_tuple(companyName, shortTermMA, longTermMA);  // Return the first tuple of values encountered
                }  
            }
        
        else {
            std::cerr << "Error: Unable to open " << filename << " for reading." << std::endl;
        }
        file.close();

        std::this_thread::sleep_for(std::chrono::seconds(1)); // Adjust the interval as needed
    }
    std::cout << "Parsed line. shortTermMA: " << shortTermMA << ", longTermMA: " << longTermMA << std::endl;
    return std::make_tuple(companyName, shortTermMA, longTermMA);  // Return the last found tuple of values, or ("", 0.0, 0.0) if no tuple was found
}
void TradingEngine::strategy(const double& shortTerm, const double& longTerm, const std::string& companyName) {
    // Implement your strategy logic here
    
    // Example strategy: buy when the short-term moving average crosses above the long-term moving average
    if (shortTerm > longTerm) {
        executeOrder("buy", 1.0, companyName);
    }
    // Example strategy: sell when the short-term moving average crosses below the long-term moving average
    else if (shortTerm <= longTerm) {
        executeOrder("sell", 1.0, companyName);
    }
    else {
        std::cerr << "Error: Invalid strategy." << std::endl;
    }
}

void TradingEngine::executeOrder(const std::string& orderType, double amount, const std::string& companyName) {
    std::ofstream file("C:\\Users\\halen\\source\\tradebook\\orders.txt", std::ios_base::app);
    if (!file) {
        std::cerr << "Error: Unable to open orders.txt for writing." << std::endl;
        return;
    }

    file << orderType << " " << amount << " " << companyName << std::endl;

    if (!file.good()) {
        std::cerr << "Error: Writing to orders.txt failed." << std::endl;
    }

    file.close();
}


int main() {
    TradingEngine engine;
    auto [companyName, shortTermMA, longTermMA] = engine.monitorFile("C:\\Users\\halen\\source\\tradebook\\monitor.txt");
    std::cout << "Company Name: " << companyName << std::endl;
    std::cout << "Short Term Moving Average: " << shortTermMA << std::endl;
    std::cout << "Long Term Moving Average: " << longTermMA << std::endl;
    engine.strategy(shortTermMA, longTermMA, companyName);
    return 0;
}
