using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

namespace Database
{
    public class Film
    {
        [BsonId]
        public ObjectId Id { get; set; }

        [BsonElement("name")]
        public string name { get; set; }

        [BsonElement("year")]
        public int year { get; set; }

        [BsonElement("director")]
        public string director { get; set; }

        [BsonElement("genre")]
        public string genre { get; set; }

        [BsonElement("summary")]
        public string summary { get; set; }
    }
}