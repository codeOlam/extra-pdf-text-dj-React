import React, { useState } from "react";
import axios from "axios";

import "./uploadPdf.css";

const upload_url = "http://127.0.0.1:8000/api/upload/";

const UploadPdf = () => {
  const [file, setFile] = useState<File>();
  const [title, setTitle] = useState("");

  const fileUpload = {
    title: title,
    pdf_doc: file,
  };

  const handleOnChangeTitleInput = (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    setTitle(event.target.value);
  };

  const handleOnChangeFileInput = (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    setFile(event.target.files![0]);
  };

  //Todo: change to async func
  const handleUploadFile = async () => {
    await axios
      .post(upload_url, fileUpload)
      .then((res) => {
        console.log("[handleUploadFile] res: ", res.data);
      })
      .catch((error) => console.log("[handleUploadFile] error:", error));
  };

  return (
    <div className="App-form">
      <p className=".App-header">Upload PDF</p>
      <form>
        <input
          type="text"
          placeholder="enter title"
          name={title}
          value={title}
          onChange={handleOnChangeTitleInput}
        />
        <input type="file" onChange={handleOnChangeFileInput} />
        <button type="submit" onClick={handleUploadFile}>
          {" "}
          Submit{" "}
        </button>
      </form>
    </div>
  );
};

export default UploadPdf;
