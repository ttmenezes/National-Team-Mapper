const teamSelector = document.getElementById('team-selector');
const worldMap = document.getElementById('world-map');
const teamForm = document.getElementById('team-query-form');
const playerList = document.getElementById('player-list');

// handle selector selection
teamSelector.addEventListener('change', (e) => {
  console.log(e.target.value);
  teamForm.setAttribute('action', `/${e.target.value}`);
});

function addPlayerToList(playerData) {
  const playerEl = document.createElement('li');
  playerEl.className = 'player-item-text';
  const playerWiki = document.createElement('a');
  playerWiki.className = 'player-name-text';
  playerWiki.href = playerData.wiki;
  playerWiki.textContent = playerData.name;
  const birthplaceEl = document.createElement('li');
  birthplaceEl.className = 'birthplace-item-text';
  birthplaceEl.textContent = `${playerData.birthplace}`;
  playerEl.appendChild(playerWiki);
  playerEl.appendChild(birthplaceEl);

  playerList.appendChild(playerEl);
}

function unitedKingdomEdgeCase(countryCode) {
  return (
    countryCode === 'EN' ||
    countryCode === 'WL' ||
    countryCode === 'SQ' ||
    countryCode === 'ND'
  );
}

window.addEventListener('resize', () => {
  console.log(
    'width: ' +
      document.documentElement.clientWidth +
      '   height: ' +
      document.documentElement.clientHeight
  );
});
