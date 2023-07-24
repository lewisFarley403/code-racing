// import React from "react";
// import { useLocation } from "react-router-dom";
// import { useEffect, useState } from "react";
// import io from "socket.io-client";
// import CodeScreen from "./CodeScreen";

// export default function HostScreen() {
//   const [playerList, setPlayerList] = useState([]);
//   useEffect(() => {
//     const socket = io("/");

//     // Listen for 'data_received' event
//     socket.on(`${gamecode}playerjoin`, (data) => {
//       console.log("Received data:", data);
//       var tempPlayerList = playerList;
//       tempPlayerList.push(data.uname);
//       console.log(tempPlayerList);
//       setPlayerList(tempPlayerList);
//       // Do something with the received data
//     });

//     // Clean up the socket connection when component unmounts
//     return () => {
//       socket.disconnect();
//     };
//   }, []);
//   let location = useLocation();
//   console.log(location);
//   let gamecode = location.state;

//   return (
//     <div>
//       <h1>host screen</h1>
//       <p>{gamecode}</p>
//       {console.log(playerList)}
//       <div>
//         {playerList.map((uname, i) => (
//           <p key={i}>{uname}</p>
//         ))}
//       </div>
//     </div>
//   );
// }

import React from "react";
import { useLocation } from "react-router-dom";
import { useEffect, useState } from "react";
import io from "socket.io-client";
import CodeScreen from "./CodeScreenComp";

export default function HostScreen() {
  const [playerList, setPlayerList] = useState([]);
  let location = useLocation();
  let gamecode = location.state;

  useEffect(() => {
    const socket = io("/");

    // Listen for 'data_received' event
    socket.on(`${gamecode}playerjoin`, (data) => {
      console.log("Received data:", data);
      // Create a new array and append the new player name
      setPlayerList((prevPlayerList) => [...prevPlayerList, data.uname]);
    });

    // Clean up the socket connection when component unmounts
    return () => {
      socket.disconnect();
    };
  }, [gamecode]); // Add 'gamecode' to the dependency array to re-establish the connection if the gamecode changes

  console.log(location);

  return (
    <div>
      <h1>host screen</h1>
      <p>{gamecode}</p>
      <div>
        {playerList.map((uname, i) => (
          <div>
            <p key={i}>{uname}</p>
            <div style={{ width: "300px", height: "300px", overflow: "false" }}>
              <CodeScreen />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
