package bintang.com.imagegrid.data.remote;

import java.util.List;

import bintang.com.imagegrid.data.model.JsonDataModel;
import io.reactivex.Observable;
import retrofit2.http.GET;
import retrofit2.http.Url;

public interface JsonAccessService {
    //@GET("/bins/s7200")
    //Observable<List<JsonDataModel>> getJsonFile();

    @GET
    Observable<List<JsonDataModel>> getJsonFile(@Url String url);
}
