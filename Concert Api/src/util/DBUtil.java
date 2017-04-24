package util;

import com.mongodb.MongoClient;

public class DBUtil {
	private static MongoClient mongoClient=null;
	
	
	public static MongoClient getMongoClient(){
		if(mongoClient!=null){
			return mongoClient;
		}else{
			 mongoClient=new MongoClient("localhost",27017);//Port can change
			 return mongoClient;
		}
	}
}
