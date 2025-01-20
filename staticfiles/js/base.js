console.log("JavaScript loaded");

// import { LOCATIONS } from './utils.js'
/* 
    Display the local postgres data in a chart using Chart.js.
    1. Gather the data
    2. Call the Chart constructor. Settings are organized in JSON.
    3. On the event of a page load, populate local weather report.
*/

/* 
    1. Gather the data:
    Referencing values from the Context Dictionary from the template for use in JavaScript.
*/
console.log('Beginning of javascript')

   const Q1_A = JSON.parse(document.getElementById('Q1_A').textContent);
   const Q1_B = JSON.parse(document.getElementById('Q1_B').textContent);
   const Q1_C = JSON.parse(document.getElementById('Q1_C').textContent);
   const Q1_D = JSON.parse(document.getElementById('Q1_D').textContent);

/* 
Chart.js for the RestAPI Consumer Chart 

Below in this file is a more detail explanation of how to use Charts.js  */

//The context for chart 1
const context = document.getElementById('chart1').getContext('2d');

// This setUp block will be assigned to the 'data' key of the 'config' block below.
const setup = {
    labels: ['Spring', 'Summer', 'Fall', 'Winter'],
    datasets: [{
        label: '# of Votes',
        data: [Q1_A, Q1_B, Q1_C, Q1_D],
        backgroundColor: [
            'rgba(255, 205, 86, 0.4)',
            'rgba(0, 128, 0, .2)',
            'rgba(160, 82, 45, 0.4)',
            'rgba(0, 0, 255, .2)'
        ],
        borderColor: [
            'rgba(255, 205, 86, 1)',
            'rgba(0, 128, 0, 1)',
            'rgba(160, 82, 45, 1)',
            'rgba(54, 162, 235, 1)'
        ],
        borderWidth: 1
    }]
}
const config = {
    type: 'pie',
    data: setup,
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
}

//Nice, simple constructor of a new Chart.js chart for our RestAPI consuming Chart.
const chart1 = new Chart( context, config );


/* Rest API Consumption example  */

//Chicago Illinois
let url_chicago = 'https://api.openweathermap.org/data/2.5/weather?q=chicago&appid=a8efcfe69258b521961181dac55090ca'
let tempChi = await getTempature(url_chicago)
console.log('Chicago is', tempChi)


// Rest API call #2,   Dekalb, Illinois
let url_Dekalb = 'https://api.openweathermap.org/data/2.5/weather?q=Dekalb&appid=a8efcfe69258b521961181dac55090ca'
let tempDekalb = await getTempature(url_Dekalb)
console.log('Dekalb is', tempDekalb)

// Rest API call #2,   Manchester, TN
let url_Manchester = 'https://api.openweathermap.org/data/2.5/weather?q=nashville&appid=a8efcfe69258b521961181dac55090ca'
let tempManchester = await getTempature(url_Manchester)
console.log('Manchester is', tempManchester)

// Rest API call #3,   Bloomington IL
let url_Bloomington = 'https://api.openweathermap.org/data/2.5/weather?q=bloomington&appid=a8efcfe69258b521961181dac55090ca'
let tempBloomington = await getTempature(url_Bloomington)
console.log('Bloomington is', tempBloomington)

// Rest API call #3,   Okeechobee, FL
let url_Okeechobee = 'https://api.openweathermap.org/data/2.5/weather?q=okeechobee&appid=a8efcfe69258b521961181dac55090ca'
let tempOkeechobee = await getTempature(url_Okeechobee)
console.log('Okeechobee is', tempOkeechobee)


async function getTempature(url) {
    
        // execute function, Storing response
        const response = await fetch(url);

        // Storing data in form of JSON
        var data = await response.json();
      
        if (response) {
            let K, F = 0
            K = data.main.temp
            F = ((K-273.15)*1.8)+32
            F = Math.round(F)
    
            return F  
        }
} 

async function getTeampature2(url) {
    fetch(URL, {
        headers:{
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
        },
    })
    .then(response => {
        return response.json() //Convert response to JSON
    })
    .then(data => {
        //Perform actions with the response data from the view
        let K, F = 0
        K = data.main.temp
        F = ((K-273.15)*1.8)+32
        F = Math.round(F)
        console.log('Temperature is ', F)

        return F  
    })
}


//The context for RestAPI Consumer Chart

/* 
Chart.js 101 

Description:
Chart objects are created with the Chart constructor. Ex: 'new Chart(context, config2)'
    context = The famous JS function getElementById references the <canvas>'s ID tag.
    config = Comprises of 3 distinct meta data objects: 1) type, 2) data, and 3) options.
        The 'data' object is called 'Setup' in the Charts.js online documentation

    In the end, we will make a simple call:
    const chart2 = new Chart( context, config );
        where config is a JSON object

    The structure really like this:
    Charts (
        context,
        config:
            type
            data: Setup    it's best to compartmentalize the values for the data key into a 
            options        variable called Setup to stay on-page with the chart.js documentation. 
            )

    Now we define these configs as JSON stored as const objects before making the call to the Charts constructor.
*/

const context2 = document.getElementById('myChart2').getContext('2d');

console.log("Chicago is ", tempChi, ".  Dekalb temp is ", tempDekalb)

const labels2 = ['Chicago, IL', 'Dekalb, IL',  'Manchester, TN', 'Bloomington, IL', 'Okeechobee, FL'];
// const labels = Utils.months({count: 7});
const setup2 = {
  labels: labels2,
  datasets: [{
    label: [''],
    data: [tempChi, tempDekalb, tempManchester, tempBloomington, tempOkeechobee ],
    backgroundColor: [
      'rgba(255, 99, 132, 0.2)',
      'rgba(255, 159, 64, 0.2)',
      'rgba(255, 205, 86, 0.2)',
      'rgba(75, 192, 192, 0.2)',
      'rgba(54, 162, 235, 0.2)',
      'rgba(153, 102, 255, 0.2)',
      'rgba(201, 203, 207, 0.2)'
    ],
    borderColor: [
      'rgb(255, 99, 132)',
      'rgb(255, 159, 64)',
      'rgb(255, 205, 86)',
      'rgb(75, 192, 192)',
      'rgb(54, 162, 235)',
      'rgb(153, 102, 255)',
      'rgb(201, 203, 207)'
    ],
    borderWidth: 1
  }]
};

// const config2 = {
//     type: 'bar',
//     data: setup2,
//     options: {
//       scales: {
//         y: {
//             suggestedMin: 0
//         }
//       }
//     },
//   };

const config2 = {
  type: 'bar',
  data: setup2,
  options: {
    responsive: true,
    plugins: {
      title: {
        display: true,
        text: 'Suggested Min and Max Settings'
      }
    },
    scales: {
      yAxes: [{
        ticks : {
            max : 100,    
            min : 0
        }
    }]
    }
  },
};


  
//Nice, simple constructor of a new Chart.js chart for our RestAPI consuming Chart.
const chart2 = new Chart( context2, config2 );
console.log('end of javascript')



/*
    3. On the event of a page load, populate local weather report.
    Stragety source: https://www.peachpit.com/articles/article.aspx?p=1394321&seqNum=2
*/

console.log("Xbop");


function onLoadFunct() {
    console.log("Page load");
    document.getElementById("weatherLocationInputID").value = "CHICAGO"; 
  }