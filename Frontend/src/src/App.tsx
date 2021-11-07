// import Documents from "./components/Documents";
import UploadPdf from "./components/UploadPdf";
import ExtractText from "./components/ExtractedText";

import "./App.css";

function App() {
  return (
    <div className="App">
      <UploadPdf />
      <div>
        {/* <Documents /> */}
        <ExtractText />
      </div>
    </div>
  );
}

export default App;
