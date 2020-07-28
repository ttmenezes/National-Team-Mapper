import teamData from "./test-data/teamData.js";

async function getTeams() {
  let response = await fetch("https://localhost:6000/teams");
  let data = await response.json();
  console.log("here" + data);
  return data;
}

// getTeams()
//   .then((data) => console.log(data))
//   .catch(console.log("fetch error"));

const teamSelector = document.getElementById("team-selector");
const worldMap = document.getElementById("world-map");

teamData.forEach((data) => {
  const newEl = document.createElement("option");
  newEl.setAttribute("value", data.id);
  newEl.textContent = data.name;
  teamSelector.appendChild(newEl);
});

let selectedTeam = "AF";

// handle selector selection
teamSelector.addEventListener("change", (e) => {
  worldMap.innerHTML = "";
  selectedTeam = e.target.value;

  const values = {};
  values[selectedTeam] = "2";

  $("#world-map").vectorMap({
    map: "world_mill",
    scaleColors: ["#C8EEFF", "#0071A4"],
    normalizeFunction: "polynomial",
    hoverOpacity: 0.7,
    hoverColor: false,
    series: {
      regions: [
        {
          scale: {
            "1": "#A3E4D7",
            "2": "#02A0DA",
          },
          attribute: "fill",
          values: values,
        },
      ],
    },
  });
});

// $(function () {
//   $("#world-map").vectorMap({
//     map: "world_mill",
//     scaleColors: ["#C8EEFF", "#0071A4"],
//     normalizeFunction: "polynomial",
//     hoverOpacity: 0.7,
//     hoverColor: false,
//     series: {
//       regions: [
//         {
//           scale: {
//             "1": "#A3E4D7",
//             "2": "#02A0DA",
//           },
//           attribute: "fill",
//           values: {
//             BR: "1",
//             RU: "2",
//           },
//         },
//       ],
//     },
//   });
// });
