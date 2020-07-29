const teamSelector = document.getElementById('team-selector');
const worldMap = document.getElementById('world-map');
const teamForm = document.getElementById('team-query-form');
const playerList = document.getElementById('player-list');

// teamData.forEach((data) => {
//   const newEl = document.createElement("option");
//   newEl.setAttribute("value", data.id);
//   newEl.textContent = data.name;
//   teamSelector.appendChild(newEl);
// });

// handle selector selection
teamSelector.addEventListener('change', (e) => {
  console.log(e.target.value);
  teamForm.setAttribute('action', `/${e.target.value}`);
});

function addPlayerToList(playerData) {
  const playerEl = document.createElement('li');
  const playerWiki = document.createElement('a');
  playerWiki.href = playerData.wiki;
  playerWiki.textContent = playerData.name;
  const birthplaceEl = document.createElement('li');
  birthplaceEl.textContent = `${playerData.birthplace}`;
  playerEl.appendChild(playerWiki);
  playerEl.appendChild(birthplaceEl);

  playerList.appendChild(playerEl);
}

// const values = {};
// values[selectedTeam] = "2";

// $("#world-map").vectorMap({
//   map: "world_mill",
//   scaleColors: ["#C8EEFF", "#0071A4"],
//   normalizeFunction: "polynomial",
//   hoverOpacity: 0.7,
//   hoverColor: false,
//   series: {
//     regions: [
//       {
//         scale: {
//           "1": "#A3E4D7",
//           "2": "#02A0DA",
//         },
//         attribute: "fill",
//         values: values,
//       },
//     ],
//   },
// });

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
