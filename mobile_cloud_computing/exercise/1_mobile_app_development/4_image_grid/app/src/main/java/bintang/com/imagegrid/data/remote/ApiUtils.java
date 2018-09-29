package bintang.com.imagegrid.data.remote;

public class ApiUtils {
    public static JsonAccessService getJsonAccessService() {
        return RetrofitClient.getClient("https://api.myjson.com/").create(JsonAccessService.class);
    }
}
