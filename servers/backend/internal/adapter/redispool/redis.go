package redispool

import (
	"context"
	"log"

	"github.com/redis/go-redis/v9"
	"github.com/spf13/viper"
)

type Option struct {
	Addr     string
	Username string
	Password string
	DB       int
}

func NewOption(conf *viper.Viper) Option {
	return Option{
		Addr:     conf.GetString("redis.host"),
		Username: conf.GetString("redis.user"),
		Password: conf.GetString("redis.password"),
		DB:       conf.GetInt("redis.database"),
	}
}

func NewRedisPool(redisOption Option) *redis.Client {
	redisPool := redis.NewClient(&redis.Options{
		Addr:     redisOption.Addr,
		Username: redisOption.Username,
		Password: redisOption.Password,
		DB:       redisOption.DB,
	})

	result, err := redisPool.Ping(context.Background()).Result()
	if err != nil {
		log.Fatalf("redis error: %v", err)
	}
	log.Println(result)

	return redisPool
}