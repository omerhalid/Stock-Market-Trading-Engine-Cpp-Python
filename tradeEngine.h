#include <vector>
#include <string>
#include <fstream>
#include <iostream>
#include <thread>
#include <chrono>
#include <sstream>

class TradingEngine {
public:
    std::tuple<std::string, double, double>  monitorFile(const std::string& filename);
    void    strategy(const double& shortTermMA, const double& longTermMA, const std::string& companyName);
    void    executeOrder(const std::string& orderType, double amount, const std::string& companyName);

private:
    // std::string lastProcessed;
    // Additional members for strategy and risk management
};