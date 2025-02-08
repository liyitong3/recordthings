/*
 Navicat Premium Data Transfer

 Source Server         : 127.0.0.1
 Source Server Type    : MySQL
 Source Server Version : 50553
 Source Host           : 127.0.0.1:3306
 Source Schema         : memory_things_system

 Target Server Type    : MySQL
 Target Server Version : 50553
 File Encoding         : 65001

 Date: 07/02/2025 16:06:49
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for thingrecord
-- ----------------------------
DROP TABLE IF EXISTS `thingrecord`;
CREATE TABLE `thingrecord`  (
  `id` int(8) NOT NULL AUTO_INCREMENT,
  `neirong` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT '内容',
  `time` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT '时间',
  `leixing` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT '事件类型',
  `user` varchar(31) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT '当事人',
  `end_time` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL COMMENT '完成时间',
  `wancheng` int(1) UNSIGNED DEFAULT 0 COMMENT '是否已完结',
  `is_deleted` int(1) UNSIGNED DEFAULT 0 COMMENT '删除标记',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 26 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin ROW_FORMAT = Dynamic;


SET FOREIGN_KEY_CHECKS = 1;
