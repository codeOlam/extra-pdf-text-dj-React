import axios from "axios";

import "./uploadPdf.css";

const documents_url = "http://127.0.0.1:8000/api/documents/";

const UploadPdf = () => {
  const handleUploadFile = () => {
    const fileUpload = {
      title: "from front end",
      pdf_doc: null,
    };

    axios
      .post(documents_url, fileUpload)
      .then((res) => {
        console.log("[handleUploadFile] res: ", res.data);
      })
      .catch((error) => console.log("[handleUploadFile] error:", error));
  };

  return (
    <div className="App-form">
      <p className=".App-header">Upload PDF</p>
      {/* <form>
        <input type="text" placeholder="enter title" />
        <input type="file" />
        <button type="submit" onClick={handleUploadFile}>
          {" "}
          Submit{" "}
        </button>
      </form> */}
      <button type="submit" onClick={handleUploadFile}>
        Submit
      </button>
    </div>
  );
};

export default UploadPdf;
