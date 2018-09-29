package bintang.com.imagegrid.data.model;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

public class JsonDataModel {

    @SerializedName("photo")
    @Expose
    private String photo;
    @SerializedName("author")
    @Expose
    private String author;
    @SerializedName("date")
    @Expose
    private String date;

    public String getPhoto() {
        return photo;
    }

    public String getAuthor() {
        return author;
    }

    public String getDate() {
        return date;
    }
}
