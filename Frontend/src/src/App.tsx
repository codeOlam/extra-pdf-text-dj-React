import Documents from "./components/Documents";
import UploadPdf from "./components/UploadPdf";

import "./App.css";

function App() {
  return (
    <div className="App">
      <UploadPdf />
      <div>
        <p>Extracted Texts</p>
        <Documents />
      </div>
    </div>
  );
}

export default App;
