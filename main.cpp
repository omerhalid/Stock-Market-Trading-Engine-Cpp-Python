#include <vector>
#include <string>
#include <fstream>
#include <iostream>
#include <thread>
#include <chrono>
#include <sstream>

class TradingEngine {
public:
    std::pair<double, double>  monitorFile(const std::string& filename);
    void    strategy(const double& shortTermMA, const double& longTermMA);
    void    executeOrder(const std::string& orderType, double amount);

private:
    // std::string lastProcessed;
    // Additional members for strategy and risk management
};

std::pair<double, double> TradingEngine::monitorFile(const std::string& filename) {
    double shortTermMA = 0.0;
    double longTermMA = 0.0;
    while (true) {
        std::ifstream file(filename);
        std::string currentLine;

        if (file) {
            while (getline(file, currentLine)) {
                // Split the line into shortTermMA and longTermMA
                std::istringstream iss(currentLine);
                if (!(iss >> shortTermMA >> longTermMA)) {
                    // Error: the line doesn't contain two double values
                    continue;
                }
                return std::make_pair(shortTermMA, longTermMA);  // Return the first pair of double values encountered
            }
        }
        file.close();

        std::this_thread::sleep_for(std::chrono::seconds(1)); // Adjust the interval as needed
    }
    return std::make_pair(shortTermMA, longTermMA);  // Return the last found pair of double values, or (0.0, 0.0) if no pair was found
}
void TradingEngine::strategy(const double& lowValue, const double& highValue) {
    // Implement your strategy logic here
    
    // Example strategy: buy when the short-term moving average crosses above the long-term moving average
    if (lowValue > highValue) {
        executeOrder("buy", 1.0);
    }
    // Example strategy: sell when the short-term moving average crosses below the long-term moving average
    else if (lowValue < highValue) {
        executeOrder("sell", 1.0);
    }
}

void TradingEngine::executeOrder(const std::string& orderType, double amount) {
    // Implement order execution logic
    // Print out the order type and amount to .txt for demonstration purposes
    std::ofstream file("orders.txt", std::ios_base::app);
    if (file) {
        file << orderType << " " << amount << std::endl;
    }
    file.close();
}

int main() {
    TradingEngine engine;
    engine.monitorFile("monitor.txt");
    return 0;
}
