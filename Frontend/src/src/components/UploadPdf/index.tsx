import React, { useState } from "react";
import axios from "axios";

import "./uploadPdf.css";

const upload_url = "http://127.0.0.1:8000/api/upload/";

const UploadPdf = () => {
  const [pdf_doc, setPdf_doc] = useState<File>();
  const [title, setTitle] = useState("");

  const handleOnChangeTitleInput = (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    setTitle(event.target.value);
  };

  const handleOnChangeFileInput = (inputFile: FileList) => {
    if (inputFile && inputFile !== null) {
      setPdf_doc(inputFile[0]);
    }
  };

  const handleUploadFile = async () => {
    const uploadData = new FormData();
    try {
      if (title && pdf_doc) {
        uploadData.append("title", title);
        uploadData.append("pdf_doc", pdf_doc!, pdf_doc?.name as string);

        await axios({
          method: "post",
          headers: { "Content-Type": "multipart/form-data" },
          data: uploadData,
          url: upload_url,
        });
      } else {
        alert("Please Select a pdf document to upload and title");
      }
    } catch (error) {
      throw error;
    }
  };

  return (
    <div className="App-form">
      <p className=".App-header">Upload PDF</p>

      <input
        type="text"
        placeholder="enter title"
        name={title}
        value={title}
        onChange={handleOnChangeTitleInput}
      />
      <input
        type="file"
        name="file"
        onChange={(e) => handleOnChangeFileInput(e.target.files as FileList)}
      />
      <button type="submit" onClick={handleUploadFile}>
        {" "}
        Submit{" "}
      </button>
    </div>
  );
};

export default UploadPdf;
