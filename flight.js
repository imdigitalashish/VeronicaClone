var baseUrl = "https://opensky-network.org/api/";

async function flightCountByCountry() {
    var current = baseUrl + "states/all";
    console.log(current);
    const response = await fetch(current);
    const responseJson = await response.json();
    let number = 0;
    responseJson["states"].forEach(value=>{
        console.log(value);
        if(value[2]=="United States") {
            number++;
        }
    });
    return number;
}