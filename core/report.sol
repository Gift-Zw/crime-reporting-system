// CrimeReportContract.sol

pragma solidity ^0.8.0;

contract CrimeReportContract {
    struct CrimeReport {
        address reporter;
        string crimeType;
        string location;
        string city;
        uint256 date;
        string suspectInformation;
        string witnessInformation;
        string reporterCell;
        string description;
        string status;
        address assignedOfficer;
        uint256 dateCreated;
    }

    mapping(uint256 => CrimeReport) public crimeReports;
    uint256 public numReports;

    function createCrimeReport(
        string memory _crimeType,
        string memory _location,
        string memory _city,
        uint256 _date,
        string memory _suspectInformation,
        string memory _witnessInformation,
        string memory _reporterCell,
        string memory _description,
        string memory _status,
        address _assignedOfficer
    ) external {
        numReports++;
        crimeReports[numReports] = CrimeReport({
            reporter: msg.sender,
            crimeType: _crimeType,
            location: _location,
            city: _city,
            date: _date,
            suspectInformation: _suspectInformation,
            witnessInformation: _witnessInformation,
            reporterCell: _reporterCell,
            description: _description,
            status: _status,
            assignedOfficer: _assignedOfficer,
            dateCreated: block.timestamp
        });
    }
}
